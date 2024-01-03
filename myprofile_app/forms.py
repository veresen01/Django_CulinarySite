from django import forms
from django.db.models.base import Model
from .models import Category, Recipe


class MyChoiceCategory(forms.ModelChoiceField):
    def label_from_instance(self, obj: Model) -> str:
        return super().label_from_instance(obj.name_category)

class FormRecipe(forms.ModelForm):
    category = MyChoiceCategory(queryset=Category.objects.all(), empty_label=None)

    class Meta:
        model = Recipe
        exclude = ['user']
        widgets = {
            'name_recipe': forms.Textarea,
            'description': forms.Textarea, 
            'ingredients': forms.Textarea,
        }

class FormRecipeUpdate(forms.ModelForm):

    category = MyChoiceCategory(queryset=Category.objects.all())
    class Meta:
        model = Recipe
        exclude = ['user']
        widgets = {
            'name_recipe': forms.Textarea,
            'description': forms.Textarea, 
            'ingredients': forms.Textarea,
        }


