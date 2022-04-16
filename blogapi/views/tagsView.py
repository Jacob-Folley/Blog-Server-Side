from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from blogapi.serializers import TagsSerializer, TagsCreateSerializer
from blogapi.models import Tags


class TagsView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single Tags
        Returns:
            Response -- JSON serialized game type"""
        try:
            tags = Tags.objects.get(pk=pk)
            serializer = TagsSerializer(tags)
            return Response(serializer.data)
        except Tags.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all Tags
        Returns:
            Response -- JSON serialized list of game types"""
        tags = Tags.objects.all()
        serializer = TagsSerializer(tags, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle post requests to Tags"""
        serializer = TagsCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update Tags"""
        try:
            tags = Tags.objects.get(pk=pk)
            serializer = TagsCreateSerializer(tags, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Tags.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete tags"""
        tags = Tags.objects.get(pk=pk)
        tags.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)