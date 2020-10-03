# Generated by Django 3.1.2 on 2020-10-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201003_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('appetizer', 'Appetizer'), ('entree', 'Entree'), ('side', 'Side Dish'), ('dessert', 'Dessert'), ('drink', 'Drink')], default='entree', max_length=10),
        ),
    ]
