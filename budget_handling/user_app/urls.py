from django.urls import path
from .views import Login, Refresh, UserRegisteration

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("refresh/", Refresh.as_view(), name="refresh"),
    path("register/", UserRegisteration.as_view(), name="register"),
]