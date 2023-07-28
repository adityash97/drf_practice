from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User
from .models import MovieRatingDetail
from .models import Token

from movielist_app.models import Genre
from movielist_app.models import Movie

from movielist_app.serializers import GenreSerializer
from movielist_app.serializers import MovieSerializer
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


def validated_mobile_number(self):
    if self.mobile_number < 10:
        raise ValidationError({"msg": "not valid mobile num"})
    return self


def likeValidator(data):
    if not data:  # if it is False
        raise ValidationError({"msg": "You must like it"})
    return data


class MovieRatingDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    comment = serializers.CharField(required=False)
    rating = serializers.IntegerField()
    like = serializers.BooleanField(required=False, validators=[likeValidator])
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

    def validate_rating(self, data):  # only one field
        if data < 4:
            raise ValidationError({"msg": "rating should be above 4"})
        return data

    def validate(self, object):   # more than one field
        if object['rating'] == 5 and object['like'] == False:
            raise ValidationError({"msg": "You must like the movie too"})
        return object


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
