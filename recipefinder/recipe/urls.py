from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('subcategory/<int:subcategory_id>/', views.subcategory, name='subcategory'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]
