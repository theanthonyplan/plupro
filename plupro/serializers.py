from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Proposal, ProposalLine, ProposalLineCategory, ProposalLineItem

class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())    # reverse association

    class Meta:
        model = User
        fields = ['id', 'username']

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'
