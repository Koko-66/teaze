"""Urls for quiz app"""
from django.urls import path
from quiz.views import (
    AddQuizView,
    # add_quiz_view,
    TakeQuizView,
    QuizListView,
    QuizDetailsView,
)

app_name = 'quiz'
urlpatterns = [
    # path('add_quiz/', add_quiz_view, name='add_quiz'),
    path('', QuizListView.as_view(), name='home'),
    path('add_quiz/', AddQuizView.as_view(), name='add_quiz'),
    path('<slug:slug>/details', QuizDetailsView.as_view(), name='quiz_details'),
    path('<slug:slug>/', TakeQuizView.as_view(), name='take_quiz'),
    ]
