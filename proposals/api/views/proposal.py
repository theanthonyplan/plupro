from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, filters
# Create your views here.
# from ..models import Product
from ... import models
from ..serializers.proposal import ProposalSerializer
# from .api.serializers.product import ProductSerializer

class ProposalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Proposal.objects.all()
    serializer_class = ProposalSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]         # enable search filtering
    filterset_fields = ['phone_number', 'is_published']                           # fields to use in filters          
    search_fields = ['name', 'customer_name', 'phone_number',]            # fields to use in search lookup
