from rest_framework import serializers
from django.contrib.auth.models import User


from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from taggit.models import Tag

class TagSerializer(TaggitSerializer, serializers.ModelSerializer):

    # tags = TagListSerializerField()
    class Meta:
        model = Tag
        fields = '__all__'
