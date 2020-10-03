from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Recipe Collector Home</h1>')

def about(request):
    return HttpResponse('<h1>About Recipe Collector</h1>')

def recipes_index(request):
    return HttpResponse('<h1>Recipes Index</h1>')

def recipe_new(request):
    return HttpResponse('<h1>New Recipe</h1>')

def recipe_detail(request):
    return HttpResponse('<h1>Recipe Details</h1>')

def recipe_edit(request):
    return HttpResponse('<h1>Edit a Recipe</h1>')