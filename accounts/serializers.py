from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import InstitutionSupervisor, User, Students



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'uuid', 'first_name', 'last_name', 'phone_number', 'password']
  


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
        read_only_fields = ("InstitutionSupervisor", "universityInspec")
