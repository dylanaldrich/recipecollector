from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Recipe

# Create your views here.
def home(request): # this will become login page
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# Books routes
def books_index(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'books/index.html', context)

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {'book':book}
    return render(request, 'books/detail.html', context)

def book_edit(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {'book':book}
    return render(request, 'books/edit.html', context)


# Chapters routes
def chapter_detail(request, chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    context = {'chapter':chapter}
    return render(request, 'chapters/detail.html', context)

def chapter_edit(request, chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    context = {'chapter':chapter}
    return render(request, 'chapters/edit.html', context)


# Recipes routes
def recipes_index(request):
    recipes = Recipe.objects.all()
    context = {'recipes':recipes}
    return render(request, 'recipes/index.html', context)

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {'recipe':recipe}
    return render(request, 'recipes/detail.html', context)

def recipe_edit(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {'recipe':recipe}
    return render(request, 'recipes/edit.html', context)