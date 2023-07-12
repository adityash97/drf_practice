from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer
from .models import Movie

class MovieList(APIView):
    #Read
    def get(self,request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
    # Write
    def post(self,request):
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # Put
    
    
    # Delete
