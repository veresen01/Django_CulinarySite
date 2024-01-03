from django.shortcuts import get_object_or_404, redirect, render
from .models import Recipe, Category
from .forms import FormRecipe, FormRecipeUpdate 
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator


@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = FormRecipe(request.POST or None, request.FILES)
        if form.is_valid():
            img_recipe = form.cleaned_data['img_recipe']
            name_recipe = form.cleaned_data['name_recipe']
            description = form.cleaned_data['description']
            ingredients = form.cleaned_data['ingredients']
            cooking_process = form.cleaned_data['cooking_process']
            category = form.cleaned_data['category']

            fs = FileSystemStorage()
            filename = fs.save(img_recipe.name, img_recipe)
            recipe = Recipe(img_recipe = filename,
                            name_recipe = name_recipe,
                            description = description,
                            ingredients = ingredients,
                            cooking_process = cooking_process,
                            user = request.user,
                            category = category)
            recipe.save()
            return redirect ('my_profile')
    else:
        form = FormRecipe()
    return render (request, 'myprofile/create_recipe.html', {'form': form})

def category_recipes(request, pk):
    category_list = Category.objects.all()
    category = Category.objects.get(pk=pk)
    recipes = Recipe.objects.filter(category = pk)
    current_page = Paginator(recipes, 4)
    page_number = request.GET.get("page")
    page_obj = current_page.get_page(page_number)
    context = {
            'recipes': recipes, 
            'category_list': category_list,
            'category': category,
            "page_obj": page_obj,
    }
    return render (request, 'maincontent/category_recipes.html', context)

def read_one_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk = int(pk))
    return render (request, 'myprofile/read_one_recipe.html', {'recipe': recipe})

def my_profile(request):
    user = request.user
    recipe_all = Recipe.objects.filter(user = user)
    current_page = Paginator(recipe_all, 4)
    page_number = request.GET.get("page")
    page_obj = current_page.get_page(page_number)
    context = {
                'user': user, 
                'recipe_all': recipe_all, 
                "page_obj": page_obj
    }
    return render (request, 'myprofile/my_profile.html', context)

def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, pk = id)
    if recipe is not None:
        recipe.delete()
    return redirect ('my_profile')

def update_recipe(request, id):
    get_recipe = get_object_or_404(Recipe, pk=id)
    if request.method == 'POST':
        form = FormRecipeUpdate(request.POST or None, request.FILES, instance=get_recipe)
        if form.is_valid():
            form.save()
            return redirect ('my_profile')
    else:
        form = FormRecipeUpdate(instance=get_recipe)
    return render (request, 'myprofile/update_recipe.html', {'form': form})



