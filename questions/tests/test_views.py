"""Tests for views in questions app."""
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User

from categories.models import Category
# from questions.views import (
#     CreateQuestionView,
#     DeleteQuestionView,
# #     DeleteOptionView,
# #     EditOptionView,
#     )
from questions.models import Question, Option
from quiz.models import Quiz


class QuestionViewsTestCase(TestCase):
    """Test Question views"""

    @classmethod
    def setUpTestData(cls):
        """Set up instance of Question and Option for testing"""
        cls.factory = RequestFactory()
        cls.user = User.objects.create_user(username='admin', password='password')
        cls.question = Question.objects.create(body='New question text',
                                               author=cls.user,
                                               quiz_id=1, status=0)
        cls.question2 = Question.objects.create(body='New question text 2',
                                                author=cls.user,
                                                quiz_id=1, status=1)
        cls.option = Option.objects.create(option='Test option 1',
                                           question=cls.question,
                                           author=cls.user, is_correct=True)
        cls.category = Category.objects.create(name='animals', author=cls.user,
                                               pk=1)                        
        cls.quiz = Quiz.objects.create(title='Test Quiz',
                                       category=cls.category,
                                       slug='test-quiz')
 

    def test_create_question_view(self):
        """Test view creating new question"""
        user = User.objects.get(pk=1)
        response = self.client.get('/questions/add_new_question/')
        self.assertEqual(response.status_code, 200)
# 
        # test post

        # https://stackoverflow.com/questions/65790933/unit-testing-in-django-for-createview
        self.client.login(username='admin', password='password')
        data = {
            'body': 'Test question',
            'author': user,
            'status': 0,
            'category': 1,
        }

        response = self.client.post('/questions/add_new_question/', data=data)
        self.assertRedirects(response, f'/questions/3/details/')
        self.assertEqual(Question.objects.filter(body='Test question').count(), 1)

    def test_create_option_view(self):
        """Test view creating new question"""

        response = self.client.get(f'/questions/add_new_question/')
        self.assertEqual(response.status_code, 200)

        # test post
        # request = self.factory.post('/questions/add_new_question/')
        # CreateQuestionView.as_view()(request)

    def test_edit_question_view(self):
        """Test edit question get success url"""
        response = self.client.post(f'/questions/{self.question.pk}/edit_question/')
        self.assertEqual(response.status_code, 200)
    
    def test_edit_option_view(self):
        """Test edit option get success url"""
        response = self.client.post(f'/questions/{self.option.pk}/edit_option/')
        self.assertEqual(response.status_code, 200)

    def test_delete_question_view(self):
        """Test delete question get success url"""
        response = self.client.post(f'/questions/delete_question/{self.question.pk}/')
        self.assertEqual(response.url, '/questions/')

    def test_delete_option_view(self):
        """Test delete option get success url"""
        response = self.client.post(f'/questions/{self.option.pk}/delete_option/')
        self.assertRedirects(response, f'/questions/{self.question.pk}/details/')

    def test_toggle_quiz_status(self):
        """Test toggling question status"""
        # test toggle if status is draft
        question = self.question
        self.client.get(f'/questions/{question.pk}/toggle/')
        updated_question = Question.objects.get(pk=question.pk)
        self.assertEqual(updated_question.status, 1)

        # test toggle if status is approved
        question2 = self.question2
        self.client.get(f'/questions/{question2.pk}/toggle/')
        updated_question2 = Question.objects.get(pk=question2.pk)
        self.assertEqual(updated_question2.status, 0)
