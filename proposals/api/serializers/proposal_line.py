from rest_framework import serializers
from django.contrib.auth.models import User

from ... import models

class ProposalLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProposalLine
        fields = '__all__'
