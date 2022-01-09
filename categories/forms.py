"""Form to create questions and answers"""
from django import forms
from .models import Category
from bootstrap_modal_forms.forms import BSModalModelForm


class NewCategoryForm(BSModalModelForm):

    class Meta:
        model = Category
        fields = (
            'name',
            'author'
        )
