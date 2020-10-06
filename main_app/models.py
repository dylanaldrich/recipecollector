from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    link = models.URLField(max_length=500)
    image = models.URLField(max_length=500)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.name