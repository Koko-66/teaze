from django.test import TestCase
from django.contrib.auth.models import User
from questions.models import Question
from quiz.models import Quiz


class QuestionTestCase(TestCase):
    """Test creation of Question object"""

    @classmethod
    def setUpTestData(cls):
        """Set up instance of Category for testing"""
        cls.user = User.objects.create_user(username='admin')
        quiz = Quiz.objects.create(pk=1, title='New Quiz')
        cls.quiz_id = quiz.pk
        cls.question = Question.objects.create(body='New question text', author=cls.user, quiz_id=cls.quiz_id)

    def test_str_method(self):
        """Test string method"""
        self.assertEqual(str(self.question), 'New question text - New Quiz')
