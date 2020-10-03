from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=150)

    APPETIZER = 'appetizer'
    ENTREE = 'entree'
    SIDE = 'side'
    SAUCE = 'sauce'
    DESSERT = 'dessert'
    DRINK = 'drink'
    RECIPE_CATEGORY_CHOICES = [
        (APPETIZER, 'Appetizer'),
        (ENTREE, 'Entree'),
        (SIDE, 'Side Dish'),
        (SAUCE, 'Sauce'),
        (DESSERT, 'Dessert'),
        (DRINK, 'Drink'),
    ]

    category = models.CharField(
        max_length=10,
        choices=RECIPE_CATEGORY_CHOICES,
        default=ENTREE,
    )
    link = models.URLField(max_length=500)
    image = models.URLField(max_length=500)

    def __str__(self):
        return self.name