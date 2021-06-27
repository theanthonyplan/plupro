from rest_framework import serializers
from django.contrib.auth.models import User


from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from taggit.models import Tag
from .models import Product

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
