from rest_framework import serializers
from django.contrib.auth.models import User


from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from taggit.models import Tag
# from ... import models



class TagSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
