from django.urls import path
from .views import StudentView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("students",StudentView, basename="students")

urlpatterns =  router.urls