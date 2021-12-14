"""Tests for quiz models"""
from django.test import TestCase
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

    def test_Quiz_string_value(self):
        self.assertEqual(str(self.quiz), 'Test Quiz')
    