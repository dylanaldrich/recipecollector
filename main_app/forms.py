from django.forms import ModelForm
from .models import Book, Chapter, Recipe

class Book_Form(ModelForm):
    class Meta:
        model = Book
        fields = ['name']


class Chapter_Form(ModelForm):
    class Meta:
        model = Chapter
        fields = [
            'name',
            'description'
        ]


class Recipe_Form(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name',
            'source',
            'link',
            'image',
            'notes',
        ]
