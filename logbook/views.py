from django.shortcuts import render
from .serializers import InstitutionSupervisorEntrySerializer,StudentsEntrySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import Entry

from django.shortcuts import  get_object_or_404


class InstitionEntry(APIView):
    class CreateEntry(APIView):
        serializer_class = InstitutionSupervisorEntrySerializer

        def get(self, request, format=None):
            get_data = Entry.objects.all()
            get_data_json = self.serializer_class(get_data, many=True)
            return Response(get_data_json.data, status=status.HTTP_200_OK)

        def post(self, request, format=None):
            serializer = InstitutionSupervisorEntrySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class SpecificEntry(APIView):
        def put(self, request, id, format=None):
            serializer = InstitutionSupervisorEntrySerializer(Entry, id=id)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, id, format=None):
            print(id)
            post = get_object_or_404(Entry, id=id)
            post.delete()
            return Response({"Status": "Deleted post"}, status=status.HTTP_200_OK)


class StudentEntry(APIView):
    class CreateEntry(APIView):
        serializer_class = StudentsEntrySerializer

        def get(self, request, format=None):
            get_data = Entry.objects.all()
            get_data_json = self.serializer_class(get_data, many=True)
            return Response(get_data_json.data, status=status.HTTP_200_OK)

        def post(self, request, format=None):
            serializer = StudentsEntrySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class SpecificEntry(APIView):
        def put(self, request, id, format=None):
            serializer = StudentsEntrySerializer(Entry, id=id)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, id, format=None):
            print(id)
            post = get_object_or_404(Entry, id=id)
            post.delete()
            return Response({"Status": "Deleted post"}, status=status.HTTP_200_OK)