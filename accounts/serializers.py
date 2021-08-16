from django.db import models
from django.db.models import fields
from rest_framework import serializers
<<<<<<< HEAD
from .models import User
from .models import InstitutionSupervisor
from .models import UniversitySupervisor

=======
>>>>>>> f421f987bfa2be4f0d59a2b1f65eaf9bc0a75f99

from .models import InstitutionSupervisor, User, Students



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'uuid', 'first_name', 'last_name', 'phone_number', 'password']
<<<<<<< HEAD


class InstitutionSupervisorSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstitutionSupervisor
        fields = ['id', 'user', 'institution']


class UniversitySupervisorSerializer(serializers.ModelSerializer):

    class Meta:
        model = UniversitySupervisor
        fields = ['id', 'user', 'university', 'department']
=======
  


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
        read_only_fields = ("InstitutionSupervisor", "universityInspec")
>>>>>>> f421f987bfa2be4f0d59a2b1f65eaf9bc0a75f99
