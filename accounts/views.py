from django.shortcuts import render
from rest_framework import permissions
from .serializers import UniversitySupervisorSerializer, UserSerializer, StudentsSerializer
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from rest_framework import viewsets
from .models import Students, UniversitySupervisor
from rest_framework.permissions import IsAuthenticated, AllowAny
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
    
class StudentView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [AllowAny]

class UniversitySupervisorView(viewsets.ModelViewSet):
    queryset = UniversitySupervisor.objects.all()
    serializer_class = UniversitySupervisorSerializer
    permission_classes = [AllowAny]