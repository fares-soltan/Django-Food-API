from rest_framework import serializers
from runapi.models import Users, Meals


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = '__all__'
