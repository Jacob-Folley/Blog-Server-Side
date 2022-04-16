from rest_framework import serializers
from blogapi.models import Blogger


class BloggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogger
        fields = ('__all__')
        depth = 3

class BloggerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogger
        fields = ['user', 'picture', 'summary']