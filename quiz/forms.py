"""Forms for quiz app"""
from django import forms
from questions.models import Question
from .models import Quiz


class NewQuizForm(forms.ModelForm):
    """Form to create new quiz."""

    STATUS = ((0, 'Draft'), (1, 'Published'))

    class Meta:
        """Meta class specifying fields."""
        model = Quiz
        fields = (
            'title',
            'category',
            'description',
            'featured_image',
        )

        widgets = {
            'title': forms.TextInput,
            'category': forms.Select,
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class AddQuestionToQuizForm(forms.ModelForm):
    """Question form class to use when adding from the quiz."""

    STATUS = ((0, 'Draft'), (1, 'Published'))

    class Meta:
        """Specify fields to use AddQuestionToQuizForm"""
        model = Question
        fields = (
            'body',
            'status',
            'feedback',
        )
