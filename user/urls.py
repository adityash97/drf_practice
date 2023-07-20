from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserAPIView, MovieRatingDetailAPIView, MovieRatingDetailsAPIView, ProfileAPIView
from .views import UserRegisterAPIView
from .views import LogoutAPIViews
urlpatterns = [
    path('', UserAPIView.as_view(), name="user_api"),
    path('mrd/', MovieRatingDetailAPIView.as_view(), name="mrd_api"),
    path('mrd/<int:pk>/', MovieRatingDetailsAPIView.as_view(), name="mrd_detail_api"),
    path('profile/', ProfileAPIView.as_view(), name="profile_api"),
    path('login/', obtain_auth_token, name="login_token"),
    path('register/', UserRegisterAPIView.as_view(), name="user_register_api"),
    path('logout/', LogoutAPIViews.as_view(), name="logout_api")

]
