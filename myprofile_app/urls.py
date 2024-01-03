from django.urls import path
from .views import(create_recipe, 
                    read_one_recipe, delete_recipe, 
                    update_recipe, my_profile, category_recipes
                )

urlpatterns = [
    path('create_recipe/', create_recipe, name='create_recipe'),
    path('read_one_recipe/<int:pk>/', read_one_recipe, name='read_one_recipe'),
    path('delete_recipe/<int:id>/', delete_recipe, name='delete_recipe'),
    path('update_recipe/<int:id>/', update_recipe, name='update_recipe'),
    path('category_recipes/<int:pk>', category_recipes, name='category_recipes'),
    path('my_profile', my_profile, name='my_profile'),
]
