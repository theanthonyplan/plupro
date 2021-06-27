from django.shortcuts import render
from rest_framework import generics, viewsets
# Create your views here.
# from ..models import Product
from ... import models
from ..serializers.product import ProductSerializer
# from .api.serializers.product import ProductSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer
