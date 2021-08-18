from django.urls import path
from .views import CreateEntry

urlpatterns = [
    path('logbook/', CreateEntry.as_view())
]
