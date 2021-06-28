from rest_framework import viewsets, serializers, permissions, authentication
from ..serializers import UserProfileSerializer
from ... import models

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Activity CRUD methods.
    """
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    lookup_field = 'user__id'
