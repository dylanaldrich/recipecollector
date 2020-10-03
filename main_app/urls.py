from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipes_index, name='recipes_index'),
    path('recipes/new/', views.recipe_new, name='recipe_new'),
    path('recipes/<int:recipe_id/', views.recipe_detail, name='recipe_detail'),
    path('recipes/<int:recipe_id/edit/', views.recipe_edit, name='recipe_edit'),
]