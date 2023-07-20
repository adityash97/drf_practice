from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer, GenreSerializer, DirectorSerializer
from .models import Movie, Genre, Director

from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MovieAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            movies = self.get_object(pk)
            many = False
        else:
            movies = Movie.objects.all()
            many = True
        movieSerializer = MovieSerializer(movies, many=many)
        return Response(movieSerializer.data)

    def post(self, request, pk=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class MovieDetailsAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        movies = self.get_object(pk)
        movieSerializer = MovieSerializer(movies, many=False)
        return Response(movieSerializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response({'msg': f'{pk} deleted'})


class GenreAPIView(APIView):
    # Post is not allowed as we have predefined values here.
    # TODO : add others field
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)


class GenreDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        genre = self.get_object(pk)
        serilaizer = GenreSerializer(genre)
        return Response(serilaizer.data)

    def put(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        genre = self.get_object(pk)
        genre.delete()
        return Response({'msg': "Sucessfully Deleted"})


class DirectorAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        director = Director.objects.all()
        serializer = DirectorSerializer(director, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DirectorDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Director.objects.get(pk=pk)
        except Director.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        director = self.get_object(pk)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)

    def put(self, request, pk):
        director = self.get_object(pk)
        serializer = DirectorSerializer(
            director, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        director = self.get_object(pk)
        director.delete()
        return Response({"msg": 'Sucessfully Deleted'})
