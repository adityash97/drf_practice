from rest_framework import serializers
from .models import Movie
from .models import Genre
from .models import Director

class MovieSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=500)
    description = serializers.CharField(required=False)
    average_rating = serializers.IntegerField(required=False)
    average_rating = serializers.IntegerField(required=False)
    total_review = serializers.IntegerField(required=False)
    released_date = serializers.DateField(required=False)
    duration = serializers.CharField(max_length=100,required=False)
    director = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all(),required=False)
    genre = serializers.PrimaryKeyRelatedField(many=True,queryset=Genre.objects.all(),required=False)
    
    def create(self,validated_data):
        genre_ids =validated_data.pop('genre',[])
        movie = Movie.objects.create(**validated_data)
        movie.genre.set(genre_ids)
        return movie
    
    def update(self,instance,validated_data):
        genre_ids = validated_data.pop('genre',[])
        for k,v in validated_data.items():
            setattr(instance,k,v)
        instance.genre.set(genre_ids)
        instance.save()
        return instance
    

class GenreSerializer(serializers.Serializer):
    genre = serializers.CharField()

class DirectorSerializer(serializers.Serializer):
    name = serializers.CharField()
    created_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()