from rest_framework import serializers
from blogapi.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('__all__')
        depth = 3

class BlogPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'picture', 'summary', 'content', 'user', 'tags']