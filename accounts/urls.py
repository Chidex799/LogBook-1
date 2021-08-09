from django.urls import path
from .views import CreateUser

urlpatterns = [
    path('register/', CreateUser.as_view(), name="register")
]