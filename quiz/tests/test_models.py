"""Tests for quiz models"""
from django.shortcuts import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from quiz.models import Quiz
from categories.models import Category
from questions.models import Question


class QuizTestCase(TestCase):
    """Test methods of Quiz object"""

    @classmethod
    def setUpTestData(cls):
        """Set up data for testing."""
        cls.user = User.objects.create_user(username='admin')
        cls.category = Category.objects.create(name='Test', author=cls.user)
        cls.quiz = Quiz.objects.create(title='Test Quiz', category=cls.category, slug='test-quiz')
        cls.quiz2 = Quiz.objects.create(title='Test Quiz 2', category=cls.category)
        cls.question = Question.objects.create(body='Question 1', author=cls.user, pk=1, quiz=cls.quiz)
        cls.question2 = Question.objects.create(body='Question 2', author=cls.user, pk=2, quiz=cls.quiz)
        cls.question3 = Question.objects.create(body='Question 3', author=cls.user, pk=3, quiz=cls.quiz2)

    def test_quiz_str_method(self):
        """Test string method"""
        self.assertEqual(str(self.quiz), 'Test Quiz')

    def test_get_questions_method(self):
        """Test method getting all quiz questions."""
        self.assertEqual(len(self.quiz.get_questions()), 2)
        self.assertEqual(len(self.quiz2.get_questions()), 1)

    def test_get_absolute_url(self):
        """Test get_absolute_url method"""
        url = reverse('quiz:quiz_details', kwargs={'slug': 'test-quiz'})
        self.assertEqual(self.quiz.get_absolute_url(), url)
