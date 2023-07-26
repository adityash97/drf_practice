from django.urls import path
from .views import MovieAPIView,MovieDetailAPI
urlpatterns = [
    path('',MovieAPIView.as_view(),name="movie"),
    path('<int:pk>/',MovieDetailAPI.as_view(),name="movie_detail") # path added
]
