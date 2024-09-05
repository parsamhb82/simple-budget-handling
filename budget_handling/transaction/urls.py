from django.urls import path
from .views import CreatTransaction

urlpatterns = [
    path('create/', CreatTransaction.as_view(), name='create_transaction'),
]