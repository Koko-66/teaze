from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from categories.models import Category
from categories.views import (
    DeleteCategoryView,
    )
from questions.models import Question
from quiz.models import Quiz


class CategoryPagesTest(TestCase):
    """"Tests for category management views."""

    @classmethod
    def setUpTestData(cls):
        
        """Set up instance of Category for testing"""
        cls.user = User.objects.create_user(username='admin', password='password', pk=1)
        cls.category = Category.objects.create(name='animals', author=cls.user, pk=1)
        cls.category1 = Category.objects.create(name='trivia', author=cls.user, pk=2)
        cls.category2 = Category.objects.create(name='books', author=cls.user, pk=3)
        cls.quiz = Quiz.objects.create(title='Test Quiz', category=cls.category, slug='test-quiz')
        cls.question = Question.objects.create(body='Question 1', author=cls.user, pk=1, quiz=cls.quiz)
        cls.question.category.set([cls.category])
    
    def test_create_category_view(self):
        "Test if category gets created"
        data = {
            'name': 'movies',
            'pk':4
        }
        self.client.login(username='admin', password='password')
        response = self.client.get('/categories/add_new_category/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/categories/add_new_category/', data=data)
        created_category = get_object_or_404(Category, pk=4)
        self.assertEqual(Category.objects.filter(name='movies').count(), 1)

    def test_delete_category_response_status(self):
        """Test delete category view"""
        # set up view
        request = RequestFactory().get('categories/delete_category.html')
        view = DeleteCategoryView()
        view.setup(request)

        DeleteCategoryView.as_view()(request, pk=1)
        response = DeleteCategoryView.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)
