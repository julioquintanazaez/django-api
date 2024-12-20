from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloWorldSerializer

class HelloWorldView(APIView):
    def get(self, request):
        data = {"message": "Hello, World!"}
        serializer = HelloWorldSerializer(data=data)
        serializer.is_valid()
        return Response(serializer.data)

