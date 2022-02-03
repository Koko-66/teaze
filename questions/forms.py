"""Form to create questions and answers"""
from django import forms
# from django.forms import widgets
from django.contrib.auth.models import User

from bootstrap_modal_forms.mixins import (
    PopRequestMixin,
    CreateUpdateAjaxMixin
)
from .models import Question, Option


class NewQuestionForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    """Question form class to use when creating a question independently."""

    STATUS = ((0, 'Draft'), (1, 'Published'))

    class Meta:
        """Specify fields to use NewQuestionForm"""
        model = Question
        fields = (
            'body',
            'quiz',
            'feedback',
            'status',
            'category',
            'featured_image',
        )

        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 3}),
        }
        
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


class EditQuestionTextForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    
    class Meta:
        """Specify fields to use in the form."""
        model = Question
        fields = (
            'body',
        )

class EditQuestionQuizForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    
    class Meta:
        """Specify fields to use in the form."""
        model = Question
        fields = (
            'quiz',
        )
    widgets = {
        'quiz': forms.Select(attrs={"class": "form-select"})
    }
   
class EditQuestionCategoryForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    
    class Meta:
        """Specify fields to use in the form."""
        model = Question
        fields = (
            'category',
        )

class EditQuestionFeedbackForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    
    class Meta:
        """Specify fields to use in the form."""
        model = Question
        fields = (
            'feedback',
        )
        widgets = {
                'feedback': forms.Textarea(attrs={'rows': 3}),
            }

# class EditQuestionStatusForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    
#     class Meta:
#         """Specify fields to use in the form."""
#         model = Question
#         fields = (
#             'status',
#         )


class EditQuestionImageForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    
    class Meta:
        """Specify fields to use in the form."""
        model = Question
        fields = (
            'featured_image',
        )