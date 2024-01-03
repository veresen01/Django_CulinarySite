from django.db import models
from user_app.models import UserAuth


class Category(models.Model):
    name_category = models.CharField(max_length=50)

class Recipe(models.Model):
    img_recipe = models.ImageField(upload_to='img_recipe')
    name_recipe = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.TextField()
    cooking_process = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(UserAuth, on_delete=models.CASCADE)