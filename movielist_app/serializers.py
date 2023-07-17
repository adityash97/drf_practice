from rest_framework import serializers
from .models import Movie
from .models import Genre
from .models import Director


class GenreSerializer(serializers.Serializer):
    genre = serializers.CharField()

    # TODO create genre.
    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance


class DirectorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Director.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=500)
    description = serializers.CharField(required=False)
    average_rating = serializers.IntegerField(required=False)
    average_rating = serializers.IntegerField(required=False)
    total_review = serializers.IntegerField(required=False)
    released_date = serializers.DateField(required=False)
    duration = serializers.CharField(max_length=100, required=False)
    director = DirectorSerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)

    def create(self, validated_data):
        genre_ids = self.initial_data['genre']
        genres = []
        for genre in genre_ids:
            try:
                genres.append(Genre.objects.get(pk=genre["id"]))
            except:
                pass
        validated_data['director'] = Director.objects.get(
            pk=self.initial_data['director']['id'])
        movie = Movie.objects.create(**validated_data)
        movie.genre.set(genres)
        return movie

    def update(self, instance, validated_data):
        genre_ids = self.initial_data['genre']
        genres = []
        for genre in genre_ids:
            try:
                genres.append(Genre.objects.get(pk=genre["id"]))
            except:
                pass

        validated_data['director'] = Director.objects.get(
            pk=self.initial_data['director']['id'])
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.genre.set(genres)
        instance.save()
        return instance
