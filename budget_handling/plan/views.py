from django.shortcuts import render
from .models import Plan
from .serializers import PlanSerializer

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class CreatPlanView(CreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]

class ViewPlan(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Plan.objects.filter(user=self.request.user)