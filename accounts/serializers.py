from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=50, min_length=8, write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'uuid', 'first_name', 'last_name', 'phone_number', 'password']
  