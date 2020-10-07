from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Book, Chapter, Recipe
from .forms import Book_Form, Chapter_Form, Recipe_Form


# Create your views here.
def home(request): # this will become login page
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# SECTION Books routes
# index && create
def books_index(request):
    if request.method == 'POST':
        book_form = Book_Form(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('books_index')
    books = Book.objects.all()
    book_form = Book_Form()
    context = {'books':books, 'book_form':book_form}
    return render(request, 'books/index.html', context)

# show
def book_detail(request, book_id): # this serves as chapters index of a given book
    book = Book.objects.get(id=book_id)
    chapter_form = Chapter_Form()
    context = {
        'book':book,
        'chapter_form':chapter_form,
    }
    return render(request, 'books/detail.html', context)

# edit && update
def book_edit(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book_form = Book_Form(request.POST, instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect('detail', book_id=book_id)
    else:
        book_form = Book_Form(instance=book)
    context = {'book':book, 'book_form':book_form}
    return render(request, 'books/edit.html', context)

# delete
def book_delete(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect('books_index')


# SECTION Chapters routes
# show
def chapter_detail(request, chapter_id): #this serves as recipes index of a given chapter
    chapter = Chapter.objects.get(id=chapter_id)
    context = {'chapter':chapter}
    return render(request, 'chapters/detail.html', context)

# create
def chapter_add(request, book_id):
    chapter_form = Chapter_Form(request.POST)
    if chapter_form.is_valid():
        new_chapter = chapter_form.save(commit=False)
        new_chapter.book_id = book_id
        new_chapter.save()
    return redirect('book_detail', book_id=book_id)

# edit && update
def chapter_edit(request, chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    context = {'chapter':chapter}
    return render(request, 'chapters/edit.html', context)

# delete
def chapter_delete(request, chapter_id):
    Chapter.objects.get(id=chapter_id).delete()
    # TODO get this to redirect back to the parent book's detail page
    return redirect('chapters_index')

# SECTION Recipes routes
def recipes_index(request): # this lists ALL recipes of current user
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

def recipe_add(request, book_id):
    recipe_form = Book_Form(request.POST)
    if recipe_form.is_valid():
        new_recipe = feeding_form.save(commit=False)
        new_recipe.book_id = book_id
        new_recipe.save()
    return redirect('detail', book_id=book_id)

def recipe_delete(request, recipe_id):
    Recipe.objects.get(id=recipe_id).delete()
    # TODO get this to redirect back to the parent book's detail page
    return redirect('recipes_index')