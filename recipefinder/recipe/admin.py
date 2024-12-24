from django.contrib import admin

from .models import Category,Subcategory,Recipe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('name','description')

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display= ('name','description')

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display= ('name','description','ingredients','steps','cook_time')