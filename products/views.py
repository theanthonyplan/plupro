from django.shortcuts import render
from rest_framework import generics, viewsets
# Create your views here.
from taggit.models import Tag
from .models import Product
from products.serializers import TagSerializer, ProductSerializer


# Create your views here.
class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
