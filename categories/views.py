"""Views to manage categories - CRUD"""
from django.urls import reverse_lazy
from django.views.generic import ListView
# views provided by django-bootstrap-modal-forms
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView
)
from quiz.models import Quiz
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
    success_message = 'Success: Category was deleted.'
    success_url = reverse_lazy('categories:manage_categories')


class CategoriesListView(ListView):
    """List all available categories."""
    model = Category
    template_name = 'categories/manage_categories.html'

    def get_context_data(self, **kwargs):
        """Get list of categories used in quizzes as additional context data"""
        context = super(CategoriesListView, self).get_context_data(**kwargs)
        # Get all categories used in quizzes
        quizzes = Quiz.objects.all()
        protected_categories = []

        for quiz in quizzes:
            protected_categories.append(quiz.category)
            print(protected_categories)

        context['protected_categories'] = protected_categories
        return context
