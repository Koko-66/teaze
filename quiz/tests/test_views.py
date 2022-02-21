"""Test Quiz views"""
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User, Group
from questions.models import Question, Option
from quiz.models import Quiz
# from quiz.views import CreateQuizView
from categories.models import Category
from results.models import Assessment



class QuizTestCase(TestCase):
    """Test methods of Quiz object"""

    @classmethod
    def setUpTestData(cls):
        """Set up instances of models for testing"""
        cls.user = User.objects.create_user(username='admin',
                                            password='password')
        cls.adminuser = User.objects.create_user(username='adminuser',
                                                 password='password')
        cls.group = Group.objects.create(name="Admin")
        cls.adminuser.groups.set([cls.group.pk])
        cls.category = Category.objects.create(name='Test', author=cls.user)
        cls.quiz = Quiz.objects.create(title='Test Quiz',
                                       category=cls.category,
                                       slug='test-quiz', status=0)
        cls.quiz2 = Quiz.objects.create(title='Test Quiz 2',
                                       category=cls.category,
                                       slug='test-quiz-2', status=1)
        cls.question = Question.objects.create(body='New question text',
                                               author=cls.user,
                                               quiz=cls.quiz, status=0)
        cls.option = Option.objects.create(option='Test option 1',
                                           question=cls.question,
                                           author=cls.user, is_correct=True)               
        cls.assessment = Assessment.objects.create(user=cls.user, quiz=cls.quiz,
                                                   score=0)

    def test_welcome_view(self):
        """Test welcome view"""
        # test redirect when not authenticated
        response = self.client.get('/')
        self.assertEqual(response.url, '/accounts/login/')
        # test when authenticated as standard user
        self.client.login(username='admin', password='password')
        response1 = self.client.get('/')
        self.assertEqual(response1.status_code, 200)
        # test when authenticated as Admin
        self.client.login(username='adminuser', password='password')
        response2 = self.client.get('/')
        print(response2)
        
    def test_create_quiz_view_get_success_url(self):
        """Test get_success_url method in CreateQuizView"""

        # self.client.login(username='adminuser', password='password')
        response = self.client.get('/quizzes/add_quiz/')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed('quiz/add_quiz.html')
        # data = {
        #     'title': 'Test quiz creation',
        #     'category': self.category,
        #     'status': 0
        # }
        # response = self.client.post('/quizzes/add_quiz/', data)
        # # self.assertEqual(Quiz.objects.filter(title='Test quiz creation').count(), 1)
        # print(response)
        # self.assertEqual(response.status_code, 200)

    def test_quiz_list_view(self):
        """Test QuizListView"""
        # test when authenticated as standard user
        self.client.login(username='admin', password='password')
        response1 = self.client.get('/quizzes/')
        print(response1)
        self.assertEqual(response1.status_code, 200)
        # test when authenticated as Admin
        self.client.login(username='adminuser', password='password')
        response2 = self.client.get('/quizzes/')
        self.assertEqual(response2.status_code, 200)
        print(response2)

    def test_edit_question_in_quiz_view(self):
        """Test get_success_url method in EditQuestionInQuizView"""
        response = self.client.post(f'/quizzes/{self.quiz.slug}/{self.question.pk}/edit_question/')
        self.assertEqual(response.status_code, 200)
    
    def test_edit_option_in_quiz_view(self):
        """Test get_success_url method in EditOptionInQuizView"""
        
        response = self.client.get(f'/quizzes/{self.quiz.slug}/{self.option.pk}/edit_option/')
        self.assertEqual(response.status_code, 200)

    def test_delete_question_in_quiz_view(self):
        """Test get success url in DeleteQuestionInQuizView"""
        response = self.client.post(f'/quizzes/{self.quiz.slug}/{self.question.pk}/delete_question/')
        self.assertRedirects(response, '/quizzes/test-quiz/details/')

    def test_delete_option_in_quiz_view(self):
        """Test delete option get success url"""
        response = self.client.post(f'/quizzes/{self.quiz.slug}/{self.option.pk}/delete_option/')
        self.assertRedirects(response, f'/quizzes/test-quiz/{self.question.pk}/details/')

    def test_toggle_question_status(self):
        """Test toggling question status"""
        # check toggle if status is draft
        quiz = self.quiz
        self.client.get(f'/quizzes/{quiz.slug}/toggle/')
        updated_quiz= Quiz.objects.get(slug=quiz.slug)
        self.assertEqual(updated_quiz.status, 1)
        # check toggle if status is published
        quiz2 = self.quiz2
        self.client.get(f'/quizzes/{quiz2.slug}/toggle/')
        updated_quiz2= Quiz.objects.get(slug=quiz2.slug)
        self.assertEqual(updated_quiz2.status, 0)