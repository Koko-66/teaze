"""Test Quiz views"""
from django.test import TestCase
from quiz.models import Quiz
from django.contrib.auth.models import User
from quiz.models import Quiz
from categories.models import Category


class QuizTestCase(TestCase):
    """Test methods of Quiz object"""

    @classmethod
    def setUpTestData(cls):
        """Set up instance of Question for testing"""
        cls.user = User.objects.create_user(username='admin')
        cls.category = Category.objects.create(name='Test', author=cls.user)
        cls.quiz = Quiz.objects.create(title='Test Quiz', category=cls.category)

    def test_quiz_view(self):
        response = self.client.get('quiz/id')
        no_response = self.client.get('quiz/12345')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)