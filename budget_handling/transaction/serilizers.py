from rest_framework import serializers
from .models import Transaction

class CreatTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'name', 'amount', 'description')