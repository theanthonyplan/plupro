from django.shortcuts import render
from rest_framework import generics, viewsets
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
