from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from ..auth import CsrfExemptSessionAuthentication
# Create your views here.
from taggit.models import Tag
from ..serializers.tag import TagSerializer


# Create your views here.
class TagViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
