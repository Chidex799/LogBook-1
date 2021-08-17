from django.urls import path
from .views import StudentView, UniversitySupervisorView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("students",StudentView, basename="students")
router.register("universitysupervisor",UniversitySupervisorView, basename="university supervisor")

urlpatterns =  router.urls