from django import forms
from cloudinary.models import CloudinaryField
from .models import Quiz


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
            'slug',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            # 'featured_image': forms.Image(attrs={'class': 'custom-file-input'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
