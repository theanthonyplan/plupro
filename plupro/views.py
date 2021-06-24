from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from .models import Proposal, ProposalLine, ProposalLineCategory, ProposalLineItem
from .serializers import UserSerializer, ProposalSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProposalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
