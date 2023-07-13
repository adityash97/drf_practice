from django.urls import path
from .views import MovieAPIView,GenreAPIView,DirectorAPIView,MovieDetailsAPIView,GenreDetailAPIView,DirectorDetailAPIView

urlpatterns = [
    path('', MovieAPIView.as_view(),name='movie_api'),
    path('<int:pk>/', MovieDetailsAPIView.as_view(),name='movie_details_api'),
    path('genre/',GenreAPIView.as_view(),name="genre_api"),
    path('genre/<int:pk>/',GenreDetailAPIView.as_view(),name="genre_detail_api"),
    path('director/',DirectorAPIView.as_view(),name="director_api"),
    path('director/<int:pk>/',DirectorDetailAPIView.as_view(),name="director_detail_api")
]
