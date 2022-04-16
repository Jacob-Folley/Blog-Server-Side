from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from blogapi.serializers import BloggerSerializer, BloggerCreateSerializer
from blogapi.models import Blogger
import uuid
import base64
from django.core.files.base import ContentFile


class BloggerView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single Blogger
        Returns:
            Response -- JSON serialized game type"""
        try:
            blogger = Blogger.objects.get(pk=pk)
            serializer = BloggerSerializer(blogger)
            return Response(serializer.data)
        except Blogger.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all Blogger
        Returns:
            Response -- JSON serialized list of game types"""
        blogger = Blogger.objects.all()
        serializer = BloggerSerializer(blogger, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle post requests to Blogger"""
        user = request.auth.user
        format, imgstr = request.data["file"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{user.username}-{uuid.uuid4()}.{ext}')
        serializer = BloggerCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(picture=data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update Blogger"""
        try:
            blogger = Blogger.objects.get(pk=pk)
            serializer = BloggerCreateSerializer(blogger, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Blogger.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete Blogger"""
        blogger = Blogger.objects.get(pk=pk)
        blogger.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)