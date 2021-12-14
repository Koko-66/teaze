"""Urls for quiz app"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.QuizList.as_view(), name='home'),
    path('<slug:slug>/', views.QuizDetails.as_view(), name='quiz_detail'),
    ]
