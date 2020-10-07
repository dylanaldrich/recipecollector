from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # this will end up being the login page
    path('about/', views.about, name='about'),

    # Book URLs
    path('books/', views.books_index, name='books_index'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'), # this lists chapters of a given book
    path('books/<int:book_id>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),
    path('books/<int:book_id>/chapter_add/', views.chapter_add, name='chapter_add'),

    # Chapter URLs 
    path('chapters/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'), # this lists recipes of given chapter
    path('chapters/<int:chapter_id>/edit/', views.chapter_edit, name='chapter_edit'),
    path('chapters/<int:chapter_id>/delete/', views.chapter_delete, name='chapter_delete'),
    

    # Recipes URLs
    path('recipes/', views.recipes_index, name='recipes_index'), # this lists all recipes of a given user
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/<int:recipe_id>/add/', views.recipe_add, name='recipe_add'),
    path('recipes/<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipes/<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),
]