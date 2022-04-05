from rest_framework import serializers
from blogapi.models import Favorites


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('__all__')
        depth = 3

class FavoritesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['blog', 'user']