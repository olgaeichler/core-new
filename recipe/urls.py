from django.urls import path
from . import views


app_name = 'recipe'

urlpatterns = [
    path('list/', views.recipes, name='recipe_list'),
    path('update_recipe/<int:id>/', views.update_recipe, name='update_recipe'),
    path('delete_recipe/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path('api_recipe/v1/', views.api_recipe, name='api_recipe'),
]