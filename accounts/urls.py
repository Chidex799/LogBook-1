from django.urls import path
from .views import StudentView, UniversitySupervisorView
from .views import StudentView, InstitutionSupervisorView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("students",StudentView, basename="students")
router.register("university/supervisor",UniversitySupervisorView, basename="university supervisor")
router.register("institution/supervisor",InstitutionSupervisorView, basename="InstitutionSupervisor")

urlpatterns =  router.urls