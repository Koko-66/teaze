from django.contrib import admin
from quiz.models import (Answers, Assessment, Category, Option, Question,
                         QuestionOptions, Quiz, QuizQuestion)


models = [Answers, Assessment, Category, Option, Question,
          QuestionOptions, Quiz, QuizQuestion]
admin.site.register(models)
