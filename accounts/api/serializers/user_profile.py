from rest_framework import serializers

from ... import models

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = "__all__"
        lookup_field = 'user__id'
