"""Views to manage categories - CRUD"""
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView
# views provided by django-bootstrap-modal-forms
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView
)
from quiz.models import Quiz
from questions.models import Question
from .forms import NewCategoryForm
from .models import Category


class AddCategoryView(BSModalCreateView):
    """Add new category."""

    template_name = 'categories/add_category.html'
    form_class = NewCategoryForm
    success_message = 'Success: Category was created.'
    success_url = reverse_lazy('categories:manage_categories')


class EditCategoryView(BSModalUpdateView):
    """Edit category."""

    model = Category
    template_name = 'categories/edit_category.html'
    form_class = NewCategoryForm
    success_message = 'Success: Category was updated.'
    success_url = reverse_lazy('categories:manage_categories')


class DeleteCategoryView(BSModalDeleteView):
    """Delete category."""

    model = Category
    template_name = 'categories/category_confirm_delete.html'
    success_message = 'Success: Category was deleted.'
    success_url = reverse_lazy('categories:manage_categories')

    def get_object(self):
        """Grab category object to perform checks."""
        category_id = self.kwargs.get('id')
        return get_object_or_404(Category, id=category_id)

    def get(self, request, *args, **kwargs):
        """Override get function."""
        category_id = self.kwargs.get('id')
        category = get_object_or_404(Category, id=category_id)
        questions = Question.objects.all()
        quizzes = Quiz.objects.all()
        protected = False
        protected_message = ''

        # Handle ProtectedError - check if category is used in questions or quizzes:
        # if yes, prevent deletion displaying message to the user,
        # if not, ask the user to confirm deletion.
        for question in questions:
            question_categories = question.get_categories()
            if str(category.name) in question_categories:
                protected_message = f"""This category is used in question
                 <strong>{question.body}</strong> and cannot be deleted."""
                protected = True

        for quiz in quizzes:
            if category == quiz.category:
                protected_message = f"""This category is used in quiz
                 <strong>{quiz.title}</strong> and cannot be deleted."""
                protected = True

        context = {
            'protected_message': protected_message,
            'protected': protected,
            'category': category,
        }
        return render(request, 'categories/category_confirm_delete.html',
                      context)


class CategoriesListView(ListView):
    """List all available categories."""

    def get(self, request):
        queryset = Category.objects.all()
        return render(request, 'categories/manage_categories.html', {
            'categories': queryset
        })
