"""Urls for quiz app"""
from django.urls import path
from quiz.views import (
    # AddQuizView,
    add_quiz_view,
    TakeQuizView,
    QuizListView,
    QuizDetailsView,
    EditQuizView,
    DeleteQuizView,
    toggle_status,
    welcome_page_view,
    remove_question_from_quiz,
    add_question_to_quiz,
)

app_name = 'quiz'
urlpatterns = [
    path('', welcome_page_view, name='home'),
    path('quizzes/', QuizListView.as_view(), name='manage_quizzes'),
    # path('add_quiz/', AddQuizView.as_view(), name='add_quiz'),
    path('add_quiz/', add_quiz_view, name='add_quiz'),
    path('quizzes/<slug:slug>/details/', QuizDetailsView.as_view(), name='quiz_details'),
    path('quizzes/<slug:slug>/', TakeQuizView.as_view(), name='take_quiz'),
    path('quizzes/<slug:slug>/edit_quiz/', EditQuizView.as_view(), name='edit_quiz'),
    path('quizzes/<slug:slug>/delete_quiz/', DeleteQuizView.as_view(), name='delete_quiz'),
    path('quizzes/<slug:slug>/toggle/', toggle_status, name='toggle'),
    path('quizzes/<slug:slug>/<int:pk>/remove_question/', remove_question_from_quiz, name='remove_question'),
    path('quizzes/<slug:slug>/<int:pk>/add_question/', add_question_to_quiz, name='add_question'),
    ]
