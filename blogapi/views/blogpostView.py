from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from blogapi.serializers import BlogPostSerializer, BlogPostCreateSerializer
from blogapi.models import BlogPost


class BlogPostView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single BlogPost
        Returns:
            Response -- JSON serialized game type"""
        try:
            blogPost = BlogPost.objects.get(pk=pk)
            serializer = BlogPostSerializer(blogPost)
            return Response(serializer.data)
        except BlogPost.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all BlogPost
        Returns:
            Response -- JSON serialized list of game types"""
        blogPost = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogPost, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle post requests to BlogPost"""
        serializer = BlogPostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update BlogPost"""
        try:
            blogPost = BlogPost.objects.get(pk=pk)
            serializer = BlogPostCreateSerializer(blogPost, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except BlogPost.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete BlogPost"""
        blogPost = BlogPost.objects.get(pk=pk)
        blogPost.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)