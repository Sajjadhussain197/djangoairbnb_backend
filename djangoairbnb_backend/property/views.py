from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Property
from .serializers import PropertySerializer

class PropertyCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(landlord=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
