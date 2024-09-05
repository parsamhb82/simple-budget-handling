from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    goal = models.DecimalField(max_digits=10, decimal_places=2)
