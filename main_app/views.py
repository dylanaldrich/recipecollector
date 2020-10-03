from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipes_index(request):
    return render(request, 'recipes/index.html')

def recipe_new(request):
    return render(request, 'recipes/new.html')

def recipe_detail(request):
    return render(request, 'recipes/detail.html')

def recipe_edit(request):
    return HttpResponse('<h1>Edit a Recipe</h1>')