"""Filters for questions app"""
import django_filters
from django import forms
from .models import Question
from categories.models import Category

class QuestionFilter(django_filters.FilterSet):
    """Set up filter for questions"""
    body = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    # quiz = django_filters.FilterSet()
    # status = django_filters.()
    class Meta:
        """Set up model and fields for filtering"""
        model = Question
        fields = ['body', 'quiz', 'status', 'category']
