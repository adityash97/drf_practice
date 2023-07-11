from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer,GenreSerializer,DirectorSerializer
from .models import Movie,Genre,Director

class MovieAPIView(APIView):
    def get(self,request):
        movies = Movie.objects.all()
        movieSerializer = MovieSerializer(movies,many=True)
        
        return Response(movieSerializer.data)

class GenreAPIView(APIView):
    def get(self,request):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre,many = True)
        return Response(serializer.data)
    
class DirectorAPIView(APIView):
    def get(self,request):
        director = Director.objects.all()
        serializer = DirectorSerializer(director,many=True)
        
        return Response(serializer.data)