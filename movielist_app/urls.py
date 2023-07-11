from django.urls import path
from .views import MovieAPIView,GenreAPIView,DirectorAPIView

urlpatterns = [
    path('', MovieAPIView.as_view(),name='movie_api'),
    path('genre/',GenreAPIView.as_view(),name="genre_api"),
    path('director/',DirectorAPIView.as_view(),name="director_api")
]
