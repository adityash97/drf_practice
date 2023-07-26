from rest_framework import serializers

from .models import Genre
from .models import Movie

class GnereSerilaizer(serializers.Serializer):
    genre = serializers.CharField(max_length=500)


    
    

class MovieSerilaizer(serializers.Serializer):
    name = serializers.CharField()
    genre = GnereSerilaizer(read_only=True,many=True)
    
    def create(self,validated_data):  #create method
        genres = self.initial_data['genre']
        
        genresInstances = []
        
        for genre in genres:
            genresInstances.append(Genre.objects.get(pk = genre['id']))
        movie = Movie.objects.create(**validated_data)
        movie.genre.set(genresInstances)
        return movie
    
    def update(self,instance,validated_data):
        try: # handling if not getting genre from frontend client
            genres = self.initial_data['genre']
            genresInstances = []
            for genre in genres:
                genresInstances.append(Genre.objects.get(pk = genre['id']))
            instance.genre.set(genresInstances)
        except:
            pass
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance
                

    

class GnereSerilaizer(serializers.Serializer):
    genre = serializers.CharField(max_length=500)

    
