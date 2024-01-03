from django.contrib import admin
from .models import Category, Recipe

@admin.register(Category)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name_category']
    ordering = ['name_category']
    search_fields = ['name_category']
    search_help_text = 'Поиск'

    fieldsets = [
        (
            'Категория',
            {
                'classes': ['wide'],
                'fields': ['name_category'],
            },
        ),
    ]




@admin.register(Recipe)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name_recipe', 'ingredients', 'description', 'cooking_process', 'category', 'user', 'date_add']
    ordering = ['name_recipe', 'ingredients', 'category', 'user', 'date_add']
    search_fields = ['name_recipe']
    search_help_text = 'Поиск по названию рецепта'
    fieldsets = [
        (
            'Изображение блюда',
            {
                'classes': ['wide'],
                'fields': ['img_recipe'],
                'description': 'Загрузка изображения',
            },
        ),

        (
            'Подробный рецепт',
            {
                'classes': ['collapse'],
                'fields': ['name_recipe', 'description', 'ingredients', 'cooking_process', 'category'],
                'description': 'Ингридиенты, ход выполнения рецепта',
            },
        ),
        (
            'Дополнительная информация',
            {
                'classes': ['collapse'],
                'fields': ['user', 'date_add'],
                'description': 'Исполнитель рецепта и дата добавления рецепта',
            },
        ),
    ]
    readonly_fields = ['date_add']