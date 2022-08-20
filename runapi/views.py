from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import MealSerializer, UsersSerializer
from .models import Users, Meals


@api_view(['GET'])
def ShowAllUsers(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GetUser(request, pk):
    user = Users.objects.get(id=pk)
    serializer = UsersSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateUser(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def UpdateUser(request, pk):
    user = Users.objects.get(id=pk)
    serializer = UsersSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def DeleteUser(request, pk):
    user = Users.objects.get(id=pk)
    user.delete()
    return Response("Item delete successfully..!")


@api_view(['GET'])
def ShowAllMeals(request):
    meals = Meals.objects.all()
    serializer = MealSerializer(meals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GetMeal(request, pk):
    meals = Meals.objects.get(id=pk)
    serializer = MealSerializer(meals, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateMeal(request):
    serializer = MealSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def UpdateMeal(request, pk):
    meals = Meals.objects.get(id=pk)
    serializer = MealSerializer(instance=meals, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def DeleteMeal(request, pk):
    user = Meals.objects.get(id=pk)
    user.delete()
    return Response("Item delete successfully..!")
