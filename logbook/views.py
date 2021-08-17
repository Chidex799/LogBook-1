from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Entry
from .serializers import EntrySerializer
from rest_framework import status


class CreateEntry(APIView):
    def get(self, request, format=None):
        get_data = Entry.objects.all()
        get_data_json = EntrySerializer(get_data, many=True)
        return Response(get_data_json.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = EntrySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def __del__(self, request, format=None):
        serializer = EntrySerializer(data=request.data)

        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
