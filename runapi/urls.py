from django.urls import path
from . import views
urlpatterns = [
    path('get-users/', views.ShowAllUsers, name="ShowAll"),
    path('get-users/<int:pk>/', views.GetUser, name="Get-Usrs"),
    path('create-user/', views.CreateUser, name="Create-User"),
    path('update-user/<int:pk>/', views.UpdateUser, name="Update-User"),
    path('delete-user/<int:pk>/', views.DeleteUser, name="Delete-User"),

    path('get-meals/', views.ShowAllMeals, name="ShowAllm"),
    path('get-meals/<int:pk>/', views.GetMeal, name="Get-Meal"),
    path('create-meal/', views.CreateMeal, name="Create-Meal"),
    path('update-meal/<int:pk>/', views.UpdateMeal, name="Update-Meal"),
    path('delete-meal/<int:pk>/', views.DeleteMeal, name="Delete-Meal"),
]
