from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id','weekNumber', 'dateTime', 'description', 'image', 'student', 'remarks']
