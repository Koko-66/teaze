"""Urls for categories app"""
from django.urls import path
from categories.views import (
    # AddCategoryView,
    CategoriesListView,
    EditCategoryView,
    DeleteCategoryView,
    add_category_view,
)

app_name = 'categories'
urlpatterns = [
    path('categories/', CategoriesListView.as_view(), name='manage_categories'),
    # path('categories/add_category/', AddCategoryView.as_view(), name='add_category'),
    path('categories/add_category/', add_category_view, name='add_category'),
    path('categories/<int:id>/edit_category/', EditCategoryView.as_view(), name='edit_category'),
    path('categories/<int:id>/delete_category/', DeleteCategoryView.as_view(), name='delete_category'),
    ]
