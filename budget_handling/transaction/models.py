from django.db import models
from user_app.models import User
class Transaction(models.Model) :
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    description = models.TextField(blan= True , null= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.
