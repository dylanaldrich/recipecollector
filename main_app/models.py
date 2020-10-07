from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=150)
    source = models.CharField(max_length=150)
    link = models.URLField(max_length=500)
    image = models.URLField(max_length=500)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Book(models.Model):
    name = models.CharField(max_length=40)
    # recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Chapter(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    recipes = models.ManyToManyField(Recipe)
    # book = models.ForeignKey(Book, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']