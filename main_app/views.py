from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Recipe

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipes_index(request):
    recipes = Recipe.objects.all()
    context = {'recipes':recipes}
    return render(request, 'recipes/index.html', context)

def recipe_new(request):
    return render(request, 'recipes/new.html')

def recipe_detail(request):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {'recipe':recipe}
    return render(request, 'recipes/detail.html')

def recipe_edit(request):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {'recipe':recipe}
    return render(request, 'recipes/edit.html', context)