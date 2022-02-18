"""Tests for results models"""
from django.test import TestCase
from django.contrib.auth.models import User
from categories.models import Category
from results.models import Assessment, Answer
from questions.models import Question, Option
from quiz.models import Quiz



class ResultsTestCase(TestCase):
    """Test methods of Assessment and Answer objects"""

    @classmethod
    def setUpTestData(cls):
        """Set up instance of Assessment and Answer for testing"""
        cls.user = User.objects.create_user(username='user')
        cls.category = Category.objects.create(name='Test', author=cls.user)
        cls.quiz = Quiz.objects.create(title='Test Quiz', category=cls.category)
        cls.question = Question.objects.create(body='New question text',
                                               author=cls.user,
                                               quiz_id=cls.quiz.pk)
        cls.assessment = Assessment.objects.create(user=cls.user, quiz=cls.quiz, score=8, pk=1)
        cls.option = Option.objects.create(option='Test option 1',
                                           question=cls.question,
                                           author=cls.user, is_correct=True)
        cls.option1 = Option.objects.create(option='Test option 2',
                                            question=cls.question,
                                            author=cls.user, is_correct=True)
        cls.option2 = Option.objects.create(option='Test option 3',
                                            question=cls.question,
                                            author=cls.user)
        cls.answer = Answer.objects.create(question=cls.question, answer=cls.option, assessment=cls.assessment,)
        cls.answer2 = Answer.objects.create(question=cls.question, answer=cls.option1, assessment=cls.assessment,)
        cls.answer3 = Answer.objects.create(question=cls.question, answer=cls.option2, assessment=cls.assessment,)

    def test_assessment_string_value(self):
        """Test string method"""
        self.assertEqual(str(self.assessment), '1: user - Test Quiz')

    def test_get_answers(self):
        """Test get_answers method"""
        self.assertEqual(len(self.assessment.get_answers()), 3)

    def test_answer_string_value(self):
        """Test string method"""
        self.assertEqual(str(self.answer), 'New question text - Test option 1')
