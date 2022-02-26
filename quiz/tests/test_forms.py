"""Tests for forms in quiz app."""
from django.test import TestCase
from django.contrib.auth.models import User
from categories.models import Category
from questions.models import Question


class QuestionsFormsTestCase(TestCase):
    """Test quiz forms"""

    @classmethod
    def setUpTestData(cls):
        """Set up instance of Category for testing"""
        cls.user = User.objects.create_user(
            username='admin', password='password')
        cls.category = Category.objects.create(
            name='animals', author=cls.user, pk=1)
        cls.question = Question.objects.create(
            body='New question text', author=cls.user, status=0, pk=1)

    def test_new_quiz_form(self):
        """Test override save method."""
        self.client.login(username='admin', password='password')
        data = {
            'title': 'Test quiz',
            'pk': 2,
            'category': self.category,
        }
        response = self.client.post('/quizzes/add_quiz/', data=data)
        self.assertEqual(response.status_code, 200)
