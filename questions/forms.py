"""Form to create questions and answers"""
from django import forms
# from django.forms import widgets
from django.contrib.auth.models import User

from bootstrap_modal_forms.mixins import (
    PopRequestMixin,
    CreateUpdateAjaxMixin
)
from .models import Question, Option


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


class NewQuestionForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    """Question form class to use when creating a question independently."""

    STATUS = ((0, 'Draft'), (1, 'Published'))

    class Meta:
        """Specify fields to use NewQuestionForm"""
        model = Question
        fields = (
            'body',
            'quiz',
            'featured_image',
            'status',
            'feedback',
            'category',
        )

        # category = forms.ModelMultipleChoiceField(
        #         queryset=Category.objects.all(),
        #         widget=forms.CheckboxSelectMultiple
        #     )

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
    """Option form class"""

    class Meta:
        """Specify fields to use NewOption"""
        model = Option
        fields = (
            'option',
            'is_correct',
            # 'position',
        )

        widgets = {
            'option': forms.TextInput,
            'is_correct': forms.CheckboxInput(attrs={
                'class': 'form-check-input'})
        }

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