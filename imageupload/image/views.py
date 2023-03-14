from rest_framework import generics, status, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from image import serializers
from core.models import Image

class ImageView(viewsets.ModelViewSet):
    """View for listing and uploading images."""
    serializer_class = serializers.ImageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Image.objects.all()

    def get_queryset(self):
        """Retrieve images for authenticated user."""
        return self.queryset.filter(owner=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def upload_image(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
