"""Urls for questions app"""
from django.urls import path
from .views import (
    # add_new_question_view,
    CreateQuestionView,
    QuestionDetailsView,
    EditQuestionView,
    EditQuestionText,
    EditQuestionQuiz,
    EditQuestionFeedback,
    EditQuestionCategory,
    EditQuestionImage,
    DeleteQuestionView,
    QuestionListView,
    toggle_question_status,
    EditOptionView,
    DeleteOptionView,
    SearchQuestionResultsView,
    CreateOptionView,
)

app_name = 'questions'

urlpatterns = [
    # urls for questions from question management views
    path('questions/', QuestionListView.as_view(), name='manage_questions'),
    path('questions/<int:pk>/details/', QuestionDetailsView.as_view(), name='question_details'),
    path('questions/add_new_question/', CreateQuestionView.as_view(), name='add_new_question'),
    # path('questions/add_new_question/', add_new_question_view, name='add_new_question'),
    path('questions/search/', SearchQuestionResultsView.as_view(), name='search_question'),
    path('questions/<int:pk>/edit_question/', EditQuestionView.as_view(), name='edit_question'),
    path('questions/delete_question/<int:pk>/', DeleteQuestionView.as_view(), name='delete_question'),
    path('questions/<int:pk>/toggle/', toggle_question_status, name='toggle_question'),
    path('questions/<int:pk>/add_option/', CreateOptionView.as_view(), name='add_option'),
    path('questions/<int:pk>/edit_option/', EditOptionView.as_view(), name='edit_option'),
    path('questions/<int:pk>/delete_option/', DeleteOptionView.as_view(), name='delete_option'),
    path('questions/<int:pk>/edit_question_text', EditQuestionText.as_view(), name='edit_question_text'),
    path('questions/<int:pk>/edit_question_quiz', EditQuestionQuiz.as_view(), name='edit_question_quiz'),
    path('questions/<int:pk>/edit_question_feedback', EditQuestionFeedback.as_view(), name='edit_question_feedback'),
    path('questions/<int:pk>/edit_question_category', EditQuestionCategory.as_view(), name='edit_question_category'),
    path('questions/<int:pk>/edit_question_image', EditQuestionImage.as_view(), name='edit_question_image'),
]

