"""Form to create questions and answers"""
from django import forms
from django.contrib.auth.models import User
from bootstrap_modal_forms.mixins import (
    PopRequestMixin,
    CreateUpdateAjaxMixin
)
from .models import Question, Option


# class NewQuestionForm(forms.ModelForm):
#     STATUS = ((0, 'Draft'), (1, 'Published'))
    
#     class Meta:
#         model = Question
#         fields = (
#             'body',
#             # 'quiz',
#             'featured_image',
#             'status',
#             'feedback',
#         )

class NewQuestionForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    """Category form class."""

    STATUS = ((0, 'Draft'), (1, 'Published'))
    
    class Meta:
        model = Question
        help_texts = {
            'category': 'Hold Shift to select more than one category.',
        }
        fields = (
            'body',
            'quiz',
            'featured_image',
            'status',
            'feedback',
            'category',
        )

    def save(self, commit=False):
        """
        Overwrites the default save method to add current user as author and
        prevents Ajax error: 'NoneType' object has no attribute 'META'
        """
        if not self.request.is_ajax():
            instance = super(CreateUpdateAjaxMixin, self).save(commit=commit)
            instance.author = User.objects.get(pk=self.request.user.pk)
            instance.save()
        else:
            instance = super(CreateUpdateAjaxMixin, self).save(commit=False)
        return instance

    
    

class NewOptionForm(forms.ModelForm):

    class Meta:
        model = Option
        fields = (
            'option',
            'is_correct',
            'position',
        )
