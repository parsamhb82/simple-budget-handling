from django.shortcuts import render
from .models import Transaction
from .serilizers import CreatTransactionSerializer, TransactionSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
class CreatTransaction(CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = CreatTransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        amount = self.request.data.get('amount')
        if user.userbudget + float(amount) < 0:
            return Response({'error': 'Not enough budget'}, status=status.HTTP_400_BAD_REQUEST)
        user.userbudget.budget += float(amount)
        serializer.save(user=self.request.user)
class ViewTransactions(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
        


