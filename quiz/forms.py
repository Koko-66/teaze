from django import forms
from cloudinary.models import CloudinaryField
from .models import Quiz
from categories.models import Category


class NewQuizForm(forms.ModelForm):
    STATUS = ((0, 'Draft'), (1, 'Published'))

    class Meta:
        model = Quiz
        fields = (
            'title',
            'category',
            'description',
            'featured_image',
            'status',
        )

        widgets = {
            'title': forms.TextInput,
            'category': forms.Select,
            'description': forms.Textarea(attrs={'rows': 3}),
        #     # 'featured_image': forms.Image(attrs={'class': 'custom-file-input'}),
        #     'status': forms.Select(attrs={'class': 'form-control'}),
        }