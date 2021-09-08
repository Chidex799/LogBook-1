from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Entry

class StudentsEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id','weekNumber', 'dateTime', 'description', 'image', 'student', 'remarks']
        read_only_fields = ['remarks']


class InstitutionSupervisorEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id','weekNumber', 'dateTime', 'description', 'student', 'remarks']

