from django.db import models
from django.contrib.auth.models import User

class UserBudget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)


