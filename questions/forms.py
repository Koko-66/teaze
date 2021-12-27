"""Form to create questions and answers"""
from django import forms
from .models import Question, Option


class NewQuestionForm(forms.ModelForm):
    STATUS = ((0, 'Draft'), (1, 'Published'))
    
    class Meta:
        model = Question
        fields = (
            'body',
            # 'quiz',
            'featured_image',
            'status',
            'feedback',
        )
    

class NewOptionForm(forms.ModelForm):

    class Meta:
        model = Option
        fields = (
            'option',
            'is_correct',
            'position',
        )
