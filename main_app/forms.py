from django.forms import ModelForm
from .models import Recipe

class Recipe_Form(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name',
            'category',
            'link',
            'image',
        ]