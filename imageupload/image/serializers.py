"""Serializers for the image API."""
from rest_framework import serializers

from core.models import Image


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images."""

    class Meta:
        model = Image
        fields = ['id', 'image', 'owner']
        read_only_fields = ['id', 'owner']
        extra_kwargs = {'image': {'required': 'True'}}
