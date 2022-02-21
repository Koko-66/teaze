"""Tests for forms in questions app."""
from django.test import TestCase
from django.contrib.auth.models import User
# from django.http import HttpRequest
from categories.models import Category
from questions.models import Question
from quiz.models import Quiz


class QuestionsFormsTestCase(TestCase):
    """Test Category form"""

    @classmethod
    def setUpTestData(cls):
        """Set up instance of Category for testing"""
        cls.user = User.objects.create_user(username='admin',
                                            password='password')
        cls.category = Category.objects.create(name='animals',
                                               author=cls.user,
                                               pk=1)
        cls.quiz = Quiz.objects.create(title='Test Quiz',
                                       category=cls.category,
                                       slug='test-quiz')
        cls.question = Question.objects.create(body='New question text',
                                               author=cls.user,
                                               quiz=cls.quiz, status=0, pk=1)

    def test_new_qustion_form(self):
        """Test override save method."""
        self.client.login(username='admin', password='password')
        data = {
            'body': 'Test',
            'category': [self.category]
            }
        response = self.client.post('/questions/add_new_question/', data=data)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_new_option_form(self):
        """Test override save method."""
        self.client.login(username='admin', password='password')
        question_pk = self.question.pk
        data = {
            'option': 'Test option',
            'pk': 2,
            }
        response = self.client.post(f'/questions/{question_pk}/add_option/',
                                    data=data)
        self.assertEqual(response.url, '../details')
