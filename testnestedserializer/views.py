from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Movie

from .serilaizers import MovieSerilaizer



class MovieAPIView(APIView):
    def get(self,request):
        queryset = Movie.objects.all()
        serilaizer = MovieSerilaizer(queryset,many=True)
        return Response(serilaizer.data)
    
    def post(self,request):
        serilaizer = MovieSerilaizer(data = request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data)
        return Response(serilaizer.errors)

from rest_framework.exceptions import ValidationError
class MovieDetailAPI(APIView):
    def get_object(self,pk):
        try:
            return Movie.objects.get(pk=pk)
        except:
            raise ValidationError({'msg':'Movie Doesnot exist'})
    
    def get(self,request,pk):
        movie = self.get_object(pk)
        serializer = MovieSerilaizer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie = self.get_object(pk=pk)
        serializer = MovieSerilaizer(movie,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,pk):
        movie = self.get_object(pk=pk)
        movie.delete()
        return Response({"msg":"Movie Deleted"})
        
    
        
