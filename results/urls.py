"""Urls for results app"""
from django.urls import path
from . import views

app_name = 'results'
urlpatterns = [
    path('quizzes/<slug:slug>/take_quiz/', views.TakeQuizView.as_view(), name='take_quiz'),
    path('quizzes/<slug:slug>/assessment-<int:pk>/results/', views.AssessmentView.as_view(), name='assessment_details'),
    ]
