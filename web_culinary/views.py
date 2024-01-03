from django.shortcuts import render
from myprofile_app.models import Category, Recipe


def list_category(request):
    for_recipe =  Recipe.objects.order_by('?')[:4]
    category_list = Category.objects.all()
    return render (request, 'home.html', {'for_recipe': for_recipe, 'category_list': category_list})