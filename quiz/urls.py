"""Urls for quiz app"""
from django.urls import path
from quiz.views import (
    AddQuizView,
    # add_quiz_view,
    TakeQuizView,
    QuizListView,
    # QuizCompletedView
)

app_name = 'quiz'
urlpatterns = [
    # path('add_quiz/', add_quiz_view, name='add_quiz'),
    path('', QuizListView.as_view(), name='home'),
    path('add_quiz/', AddQuizView.as_view(), name='add_quiz'),

    # path('', QuizCompletedView.as_view()),
    path('<slug:slug>/', TakeQuizView.as_view(), name='take_quiz'),
    ]
