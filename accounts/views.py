from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User

# Create your views here.

class CreateUser(APIView):

    def get(self, request, format=None):
        get_data = User.objects.all()
        get_data_json = UserSerializer(get_data, many=True)
        return Response(get_data_json.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



