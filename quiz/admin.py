from django.contrib import admin
from .models import *


models = [Category, Question, Option, Quiz, QuizQuestion]
admin.site.register(models)
