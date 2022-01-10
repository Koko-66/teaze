"""Urls for categories app"""
from django.urls import path
from categories.views import (
    AddCategoryView,
    CategoriesListView,
    EditCategoryView,
    DeleteCategoryView,
)

app_name = 'categories'
urlpatterns = [
    path('categories/', CategoriesListView.as_view(), name='manage_categories'),
    path('categories/add_category/', AddCategoryView.as_view(), name='add_category'),
    path('categories/edit_category/<int:pk>/', EditCategoryView.as_view(), name='edit_category'),
    path('categories/delete_category/<int:id>/', DeleteCategoryView.as_view(), name='delete_category'),
    ]
