from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=150)
    link = models.URLField(max_length=300)
    image = models.ImageField()

    def __str__(self):
        return.self.name