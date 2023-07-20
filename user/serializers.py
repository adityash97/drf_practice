from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User
from .models import MovieRatingDetail

from movielist_app.models import Genre
from movielist_app.models import Movie


from movielist_app.serializers import MovieSerializer
from rest_framework.serializers import ModelSerializer


class ProfileSerilaizer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser',
                   'is_staff', 'user_permissions', 'groups']


# To Register
class UserResisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        exclude = ['is_superuser',
                   'is_staff', 'user_permissions', 'groups', 'last_login']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, object):
        if object["password"] != object["password2"]:
            raise ValidationError({"msg": "Please re-enter corerct password."})
        if User.objects.filter(email=object["email"]).exists():
            raise ValidationError({"msg": "Email already used!"})
        return object

    def save(self):
        user = User(
            username=self.validated_data['username'], email=self.validated_data['email'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


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
