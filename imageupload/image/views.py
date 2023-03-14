from rest_framework import generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from image import serializers


class ImageView(generics.CreateAPIView):
    """View for uploading images."""
    serializer_class = serializers.ImageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['POST'], detail=False)
    def upload_image(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
