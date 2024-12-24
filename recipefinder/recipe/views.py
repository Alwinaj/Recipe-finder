from django.shortcuts import render, get_object_or_404
from .models import Category, Subcategory, Recipe

def home(request):
    categories = Category.objects.all()
    return render(request, 'recipe/home.html', {'categories': categories})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.subcategories.all()
    return render(request, 'recipe/category.html', {'category': category, 'subcategories': subcategories})

def subcategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategory, id=subcategory_id)
    recipe = subcategory.recipe.all()
    return render(request, 'recipe/subcategory.html', {'subcategory': subcategory, 'recipe': recipe})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})
