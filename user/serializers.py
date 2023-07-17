from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User
from .models import MovieRatingDetail
from .models import Token

from movielist_app.models import Genre
from movielist_app.models import Movie

from movielist_app.serializers import GenreSerializer
from movielist_app.serializers import MovieSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fname = serializers.CharField(max_length=250)
    lname = serializers.CharField(max_length=250)
    mobile = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(required=False)
    dob = serializers.DateField(required=False)
    age = serializers.IntegerField(required=False)
    prefered_genre = GenreSerializer(many=True)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        genre_data = validated_data.pop('prefered_genre', [])
        instance = User.objects.create(**validated_data)
        geners = []
        if genre_data:
            for data in genre_data:
                genre = Genre.objects.get_or_create(genre=data['genre'])
                geners.append(genre[0])
            instance.prefered_genre.set(geners)

        return instance

    def update(self, instance, validated_data):
        genre_data = validated_data.pop('prefered_genre', [])
        if validated_data:
            for k, v in validated_data.items():
                setattr(instance, k, v)
        if genre_data:
            # 1st way
            # genre = instance.prefered_genre
            # genre.clear()
            # for data in genre_data:
            #     genre = Genre.objects.create(**data)
            #     instance.prefered_genre.add(genre)
            # 2nd way
            geners = []
            for data in genre_data:
                genre = Genre.objects.get_or_create(genre=data['genre'])
                geners.append(genre[0])
            instance.prefered_genre.set(geners)
        instance.save()
        return instance


class MovieRatingDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    comment = serializers.CharField(required=False)
    rating = serializers.IntegerField()
    like = serializers.BooleanField(required=False)
    created_on = serializers.DateTimeField(required=False)
    updated_on = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        try:
            movie = Movie.objects.get(pk=self.initial_data['movie']['id'])
            user = User.objects.get(pk=self.initial_data['user']['id'])
            validated_data['movie'] = movie
            validated_data['user'] = user
            return MovieRatingDetail.objects.create(**validated_data)
        except:
            raise ValidationError('Movie and User are required')

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance


class TokenSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    token = serializers.CharField(max_length=500, read_only=True)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        try:
            user = User.objects.get(pk=self.initial_data['user']['id'])
            validated_data['user'] = user
            token = 'sample token'  # functionality to create JWT token / simple token
            validated_data['token'] = token
            return Token.objects.create(**validated_data)
        except:
            raise ValidationError('User is required')
