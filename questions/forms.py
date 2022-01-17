"""Form to create questions and answers"""
from django import forms
from django.forms import widgets
from django.contrib.auth.models import User

from bootstrap_modal_forms.mixins import (
    PopRequestMixin,
    CreateUpdateAjaxMixin
)
from categories.models import Category
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

        # code from https://stackoverflow.com/questions/54048741/nonetype-object-has-no-attribute-is-ajax
        if not self.request.is_ajax():
            instance = super(CreateUpdateAjaxMixin, self).save(commit=commit)
            instance.author = User.objects.get(pk=self.request.user.pk)
            instance.save()
            self.save_m2m()
        else:
            instance = super(CreateUpdateAjaxMixin, self).save(commit=False)
        return instance


class NewOptionForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):

    class Meta:
        model = Option
        fields = (
            'option',
            'is_correct',
            'position',
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