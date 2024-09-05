from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserBudget

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class UserBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBudget
        fields = ('user', 'budget')