from django.contrib import admin
from .models import Book, Chapter, Recipe

# Register your models here.
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Recipe)