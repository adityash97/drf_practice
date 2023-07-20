# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from .permissions.custompermission import isAuthor
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.validators import ValidationError

from .models import User, MovieRatingDetail
from .serializers import UserSerializer
from .serializers import MovieRatingDetailSerializer
from .serializers import UserResisterSerializer
from .serializers import ProfileSerilaizer

from .models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
# To logout


class LogoutAPIViews(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # token = Token.objects.get(user=request.user)
        # token.delete()
        # return Response({"msg": "log out !"})
        request.user.auth_token.delete()
        return Response({"msg": "logged out!"}, status=HTTP_200_OK)


# To view profile


class ProfileAPIView(APIView):
    def get(self, request):
        try:
            user = request.user.username
            data = User.objects.get(username=user)
            serilaizer = ProfileSerilaizer(data)
            return Response(serilaizer.data)
        except:
            raise ValidationError({"msg": "User not found"})

# To view all users, only Admin can view it


class UserAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

# To Register A new user


class UserRegisterAPIView(APIView):
    def post(self, request):
        serializer = UserResisterSerializer(data=request.data)
        if serializer.is_valid():
            data = {}
            serializer.save()
            data['msg'] = "Register Succesfully"
            data['userdetails'] = serializer.data
            data['token'] = Token.objects.get_or_create(
                user=User.objects.get(username=serializer.data['username']))[0].key
            return JsonResponse(data)
        return Response(serializer.errors)


class MovieRatingDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
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
