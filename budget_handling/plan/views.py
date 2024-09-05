from django.shortcuts import render
from .models import Plan
from .serializers import PlanSerializer

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from user_app.models import UserBudget

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

class AddMoneyToPlanView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user
        plan_id = request.data.get('plan_id')
        amount = request.data.get('amount')

        if not plan_id or not amount:
            return Response({'error': 'Missing plan_id or amount'}, status=status.HTTP_400_BAD_REQUEST)
        if user.userbudget.budget < float(amount):
            return Response({'error': 'Not enough budget'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            plan = Plan.objects.get(id=plan_id, user=request.user)
        except Plan.DoesNotExist:
            return Response({'error': 'Plan not found'}, status=status.HTTP_404_NOT_FOUND)
        if plan.amount + float(amount) > plan.goal:
            return Response({'error': 'Cannot add more money than the goal'}, status=status.HTTP_400_BAD_REQUEST)
        plan.amount += float(amount)
        plan.save()
        user.userbudget.budget -= float(amount)
        return Response({'message': 'Money added to plan successfully'}, status=status.HTTP_200_OK)