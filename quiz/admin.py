from django.contrib import admin
from .models import Category, Question
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Category)

@admin.register(Question)
class QuestionAdmin(SummernoteModelAdmin):

    summernote_fields = ('body')
