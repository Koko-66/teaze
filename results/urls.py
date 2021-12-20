"""Urls for results app"""
from django.urls import path
from . import views

app_name = 'results'
urlpatterns = [
    path('<slug:slug>/results/', views.results, name='results'),
    # path('<slug:slug>/results/', views.ResultsDetailsView.as_view(), name='results_details'),
    ]
