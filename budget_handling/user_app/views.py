from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserSerializer, UserBudgetSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserBudget
from .serializers import UserSerializer, UserBudgetSerializer


class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass

class UserRegisteration(APIView):
    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            UserBudget.objects.create(user=user, budget=0)
            return Response({'status': 'User registered and budget created'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)