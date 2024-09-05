from django.urls import path
from .views import CreatPlanView, ViewPlan, AddMoneyToPlanView

urlpatterns = [
    path('create/', CreatPlanView.as_view(), name='create-plan'),
    path('view/', ViewPlan.as_view(), name='view-plan'),
    path('add-money/', AddMoneyToPlanView.as_view(), name='add-money-to-plan'),
]