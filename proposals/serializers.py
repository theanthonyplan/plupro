from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Proposal, ProposalLine, ProposalLineCategory
from proposals.models import Proposal

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'
