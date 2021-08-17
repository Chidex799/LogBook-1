from django.shortcuts import render
from .serializers import EntrySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import serializers, status

# Create your views here.
class SpecificEntry(APIView):
    def put(self, request, format=None):
        serializer = EntrySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

