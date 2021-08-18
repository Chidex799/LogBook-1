from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Entry
from .serializers import EntrySerializer
from rest_framework import status
from django.shortcuts import  get_object_or_404


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

    def delete(self, request, id, format=None):
        print(id)
        post = get_object_or_404(Entry, id=id)
        post.delete()
        return Response({"Status": "Deleted post"}, status=status.HTTP_200_OK)
