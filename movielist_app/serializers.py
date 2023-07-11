from rest_framework import serializers
from .models import Movie
from .models import Genre
from .models import Director

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    description = serializers.CharField()
    average_rating = serializers.IntegerField(default=0)
    total_like = serializers.IntegerField(default=0)
    total_review = serializers.IntegerField(default=0)
    released_date = serializers.DateField()
    duration = serializers.CharField(max_length=100)
    director = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all())
    genre = serializers.PrimaryKeyRelatedField(many=True,queryset=Genre.objects.all())

class GenreSerializer(serializers.Serializer):
    genre = serializers.CharField()

class DirectorSerializer(serializers.Serializer):
    name = serializers.CharField()
    created_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()