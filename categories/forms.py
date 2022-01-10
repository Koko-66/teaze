"""Form to create questions and answers"""
from django import forms
from django.contrib.auth.models import User
from bootstrap_modal_forms.mixins import (
    PopRequestMixin,
    CreateUpdateAjaxMixin
)
from .models import Category


class NewCategoryForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    """Category form class."""

    class Meta:
        """Set fields to show in the form."""
        model = Category
        fields = (
            'name',
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
