# Create your views here.
from .permissions.custompermission import isAuthor
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.validators import ValidationError

from .models import User, MovieRatingDetail, Token
from .serializers import UserSerializer
from .serializers import MovieRatingDetailSerializer
from .serializers import TokenSerializer
from .serializers import ProfileSerilaizer

from .models import User


class ProfileAPIView(APIView):
    def get(self, request):
        try:
            user = request.user.username
            data = User.objects.get(username=user)
            serilaizer = ProfileSerilaizer(data)
            return Response(serilaizer.data)
        except:
            raise ValidationError({"msg": "User not found"})


# depricated
class UserAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serilaizer = UserSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data)
        return Response(serilaizer.errors)


# depricated
class UserDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response({'msg': "User Deleted"})


class MovieRatingDetailAPIView(APIView):
    mrd = MovieRatingDetail.objects.all()

    def get(self, request):
        serializer = MovieRatingDetailSerializer(self.mrd, many=True)
        return Response(serializer.data)

    def post(self, request):
        # A user can only post one review for a movie.
        try:
            MovieRatingDetail.objects.get(
                user=request.data['user'], movie=request.data['movie'])
            return Response({'msg': 'A user can only give only review.', 'status': 400}, status=400)
        except:
            serializer = MovieRatingDetailSerializer(
                self.mrd, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)


class MovieRatingDetailsAPIView(APIView):
    permission_classes = [isAuthor]

    def get_object(self, pk):
        try:
            return MovieRatingDetail.objects.get(pk=pk)
        except MovieRatingDetail.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mrd = self.get_object(pk)
        serializer = MovieRatingDetailSerializer(mrd)
        return Response(serializer.data)

    def put(self, request, pk):
        mrd = self.get_object(pk)
        request_data = request.data
        serilaizer = MovieRatingDetailSerializer(
            mrd, data=request_data, partial=True)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data)
        return Response(serilaizer.errors)

    def delete(self, request, pk):
        mrd = self.get_object(pk)
        mrd.delete()
        return Response({"msg": "Movie Rating Details Sucessfully Deleted"})


class TokenAPIView(APIView):
    def get(self, request):
        token = Token.objects.all()
        serializer = TokenSerializer(token, many=True)
        return Response(serializer.data)

    # This should be handled by other function or if  manually then there should be only one token.
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
