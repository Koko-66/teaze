"""Urls for questions app"""
from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('questions/', views.search, name='manage_questions'),
    path('questions/<int:pk>/details/', views.QuestionDetailsView.as_view(),
         name='question_details'),
    path('questions/add_new_question/', views.CreateQuestionView.as_view(),
         name='add_new_question'),
    path('questions/<int:pk>/edit_question/', views.EditQuestionView.as_view(),
         name='edit_question'),
    path('questions/delete_question/<int:pk>/', views.DeleteQuestionView.as_view(),
         name='delete_question'),
    path('questions/<int:pk>/toggle/', views.toggle_question_status,
         name='toggle_question'),
    path('questions/<int:pk>/add_option/', views.CreateOptionView.as_view(),
         name='add_option'),
    path('questions/<int:pk>/edit_option/', views.EditOptionView.as_view(),
         name='edit_option'),
    path('questions/<int:pk>/delete_option/', views.DeleteOptionView.as_view(),
         name='delete_option'),
    path('questions/<int:pk>/edit_question_text/',
         views.EditQuestionText.as_view(), name='edit_question_text'),
    path('questions/<int:pk>/edit_question_quiz/',
         views.EditQuestionQuiz.as_view(), name='edit_question_quiz'),
    path('questions/<int:pk>/edit_question_feedback/',
         views.EditQuestionFeedback.as_view(), name='edit_question_feedback'),
    path('questions/<int:pk>/edit_question_category/',
         views.EditQuestionCategory.as_view(), name='edit_question_category'),
    path('questions/<int:pk>/edit_question_image/',
         views.EditQuestionImage.as_view(), name='edit_question_image'),
]

