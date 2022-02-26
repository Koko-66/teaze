"""Tests for results views"""
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from categories.models import Category
from questions.models import Question, Option
from quiz.models import Quiz
from results.models import Assessment, Answer
from results.views import TakeQuizView


class ResultsFunctionTestCase(TestCase):
    """Test methods of Assessment and Answer objects"""

    @classmethod
    def setUpTestData(cls):
        """Set up instance of Assessment and Answer for testing"""
        cls.user = User.objects.create_user(username='user')
        cls.category = Category.objects.create(name='Test', author=cls.user)
        cls.quiz = Quiz.objects.create(title='Test Quiz',
                                       category=cls.category,
                                       slug='test-quiz')
        cls.question = Question.objects.create(body='New question text',
                                               author=cls.user,
                                               quiz_id=cls.quiz.pk)
        cls.option = Option.objects.create(option='Test option 1',
                                           question=cls.question,
                                           author=cls.user, is_correct=True)
        cls.assessment = Assessment.objects.create(user=cls.user,
                                                   quiz=cls.quiz,
                                                   score=8)
        cls.answer = Answer.objects.create(question=cls.question,
                                           answer=cls.option,
                                           assessment=cls.assessment)

    def test_take_quiz_view_get_method(self):
        """Test TakeQuizView get method"""
        # set up view
        request = RequestFactory().get('results/take_quiz.html')
        view = TakeQuizView()
        view.setup(request)

        TakeQuizView.as_view()(request, slug='test-quiz')
        response = TakeQuizView.as_view()(request, slug='test-quiz')
        self.assertEqual(response.status_code, 200)

    def test_take_quiz_view_post_method(self):
        """Test TakeQuizView post method"""
        # set up view
        request = RequestFactory().post('results/take_quiz.html')
        request.user = self.user
        view = TakeQuizView()
        view.setup(request)

        TakeQuizView.as_view()(request, slug='test-quiz')
        response = TakeQuizView.as_view()(request, slug='test-quiz')
        self.assertEqual(response.status_code, 200)
