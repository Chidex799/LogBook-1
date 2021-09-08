from django.urls import path
from .views import InstitionEntry,StudentEntry

urlpatterns = [
    path('institution/logbook/', InstitionEntry.as_view()),
    path('student/logbook/', StudentEntry.as_view())
]
