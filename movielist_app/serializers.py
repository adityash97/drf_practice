from rest_framework import serializers
from .models import Movie
from .models import Genre
from .models import Director

from rest_framework.exceptions import ValidationError


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

# validator


def minLength(data):
    if len(data) < 5:
        raise ValidationError("Please give little more description")
    return data


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=500)
    description = serializers.CharField(required=False, validators=[minLength])
    average_rating = serializers.IntegerField(required=False)
    average_rating = serializers.IntegerField(required=False)
    total_review = serializers.IntegerField(required=False)
    released_date = serializers.DateField(required=False)
    duration = serializers.CharField(max_length=100, required=False)
    director = DirectorSerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)

    # field level validation
    def validate_title(self, data):
        if Movie.objects.filter(title=data):
            raise ValidationError({"msg": "Movie title already exit!"})
        return data

    # object level validation
    def validate(self, object):
        for field in object:
            if field == 'description' and '@' in object[field]:
                raise ValidationError(
                    {"msg": "Description must not contain '@' "})

    def create(self, validated_data):
        try:
            validated_data['director'] = Director.objects.get(
                pk=self.initial_data['director']['id'])
        except:
            raise ValidationError({"msg": "Director is required"})

        movie = Movie.objects.create(**validated_data)
        try:
            genre_ids = self.initial_data['genre']  # TODO Try catch
            genres = []
            for genre in genre_ids:
                genres.append(Genre.objects.get(pk=genre["id"]))
            movie.genre.set(genres)

        except:
            pass
        return movie

    def update(self, instance, validated_data):
        try:
            validated_data['director'] = Director.objects.get(
                pk=self.initial_data['director']['id'])
        except:
            pass

        for k, v in validated_data.items():
            setattr(instance, k, v)
        try:
            genre_ids = self.initial_data['genre']
            genres = []
            for genre in genre_ids:
                genres.append(Genre.objects.get(pk=genre["id"]))
            instance.genre.set(genres)
        except:
            pass
        instance.save()
        return instance
