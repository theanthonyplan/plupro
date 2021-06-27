from rest_framework import serializers
from django.contrib.auth.models import User

#
# from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from ... import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
