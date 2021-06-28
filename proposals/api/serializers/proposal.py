from rest_framework import serializers
from django.contrib.auth.models import User

from ... import models

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Proposal
        fields = '__all__'
