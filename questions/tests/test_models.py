"""Test for questions models"""

from django.test import TestCase
from django.contrib.auth.models import User
from categories.models import Category
from questions.models import Question, Option
from quiz.models import Quiz


class QuestionTestCase(TestCase):
    """Test Question object methods"""

    @classmethod
    def setUpTestData(cls):
        """Set up instance of Category and Option for testing"""

        cls.user = User.objects.create_user(username='admin')
        cls.category = Category.objects.create(name='Test', author=cls.user)
        cls.quiz = Quiz.objects.create(title='New Quiz',
                                       category=cls.category)
        cls.question = Question.objects.create(body='New question text',
                                               author=cls.user,
                                               quiz_id=cls.quiz.pk)
        cls.option = Option.objects.create(option='Test option 1',  
                                           question=cls.question, position=1,
                                           author=cls.user)

    def test_question_str_method(self):
        """Test string method"""

        self.assertEqual(str(self.question), 'New question text - New Quiz')

    # def test_get_options_method(self):
    #     """Test method for getting options"""

    def test_option_str_method(self):
        """Test string method"""

        self.assertEqual(str(self.option), 'Test option 1')
