"""Urls for quiz app"""
from django.urls import path
from quiz.views import (
    # main
    welcome_page_view,
    # quiz views
    add_quiz_view,
    # TakeQuizView,
    QuizListView,
    QuizDetailsView,
    EditQuizView,
    DeleteQuizView,
    AddCategoryInQuizView,
    toggle_status,
    # views to manipulate other objects in quiz views
    remove_question_from_quiz,
    add_question_to_quiz,
    add_question_view,
    add_option_view,
    QuestionDetailsView,
)

app_name = 'quiz'
urlpatterns = [
    path('', welcome_page_view, name='home'),
    path('quizzes/', QuizListView.as_view(), name='manage_quizzes'),
    path('add_quiz/', add_quiz_view, name='add_quiz'),
    path('quizzes/<slug:slug>/details/', QuizDetailsView.as_view(), name='quiz_details'),
    # path('quizzes/<slug:slug>/take-quiz', TakeQuizView.as_view(), name='take_quiz'),
    path('quizzes/<slug:slug>/edit_quiz/', EditQuizView.as_view(), name='edit_quiz'),
    path('quizzes/<slug:slug>/delete_quiz/', DeleteQuizView.as_view(), name='delete_quiz'),
    path('quizzes/<slug:slug>/toggle/', toggle_status, name='toggle'),
    path('quizzes/<slug:slug>/<int:pk>/remove_question/', remove_question_from_quiz, name='remove_question'),
    path('quizzes/<slug:slug>/<int:pk>/add_question/', add_question_to_quiz, name='add_question'),
    path('quizzes/add_category', AddCategoryInQuizView.as_view(), name='add_category_in_quiz'),
    path('quizzes/<slug:slug>/add_question/', add_question_view, name='add_question_in_quiz'),
    path('quizzes/<slug:slug>/<int:pk>/add_option/', add_option_view, name='add_option_in_quiz'),
    path('quizzes/<slug:slug>/<int:pk>/details/', QuestionDetailsView.as_view(), name='quiz_question_details'),
    ]
