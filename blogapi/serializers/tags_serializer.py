from rest_framework import serializers
from blogapi.models import Tags


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('__all__')
        depth = 3

class TagsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['name']