from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from blogapi.serializers import FavoritesSerializer, FavoritesCreateSerializer
from blogapi.models import Favorites


class FavoritesView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single Favorites
        Returns:
            Response -- JSON serialized game type"""
        try:
            favorites = Favorites.objects.get(pk=pk)
            serializer = FavoritesSerializer(favorites)
            return Response(serializer.data)
        except Favorites.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all Favorites
        Returns:
            Response -- JSON serialized list of game types"""
        favorites = Favorites.objects.all()
        serializer = FavoritesSerializer(favorites, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle post requests to Favorites"""
        serializer = FavoritesCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update Favorites"""
        try:
            favorites = Favorites.objects.get(pk=pk)
            serializer = FavoritesCreateSerializer(favorites, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Favorites.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete Favorites"""
        favorites = Favorites.objects.get(pk=pk)
        favorites.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)