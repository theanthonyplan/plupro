from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from proposals.models import Proposal
from proposals.serializers import ProposalSerializer
# Create your views here.
class ProposalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
