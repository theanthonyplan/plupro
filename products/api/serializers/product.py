from rest_framework import serializers
from django.contrib.auth.models import User

#
# from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from ... import models
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from .tag import TagSerializer

class ProductSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = models.Product
        fields = '__all__'
