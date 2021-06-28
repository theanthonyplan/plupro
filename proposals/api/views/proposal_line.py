from django.shortcuts import render
from rest_framework import generics, viewsets
# Create your views here.
# from ..models import Product
from ... import models
from ..serializers.proposal_line import ProposalLineSerializer
# from .api.serializers.product import ProductSerializer

class ProposalLineViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.ProposalLine.objects.all()
    serializer_class = ProposalLineSerializer
