from django.shortcuts import render
from rest_framework import generics, viewsets, filters
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from ..auth import CsrfExemptSessionAuthentication
# Create your views here.
# from ..models import Product
from ... import models
from ..serializers.product import ProductSerializer
# from .api.serializers.product import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    serializer_class = ProductSerializer
    queryset = models.Product.objects.all()
    filter_backends = [filters.SearchFilter]        # enable search filtering
    search_fields = ['name', 'description', 'tags__name']                # fiels to use in lookup


    # consider adding custom logic for retagging products
