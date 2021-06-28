from django.utils import timezone

from rest_framework import viewsets, serializers, permissions, authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action

from .. import serializers
from ... import models
from ..auth import CsrfExemptSessionAuthentication
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)  # TODO, fix
    authentication_classes = (CsrfExemptSessionAuthentication,) # TODO, fix
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    # def get_queryset(self):
    #     questionnaire_id = self.request.GET.get("questionnaire_id")
    #     return self.queryset.filter(questionnaire_id=questionnaire_id, user=self.request.user.id)

    @action(methods=["put"], detail=True)
    def update_profile(self, request, pk=None):
        instance = self.get_object() 

        errors = []       
        payload = request.data
        print(payload)
        profile_payload = payload['profile']
        profile_ser = serializers.UserProfileSerializer(instance.userprofile, data=profile_payload, partial=True)
        if profile_ser.is_valid():
            profile_ser.save()
        else:
            errors.extend(profile_ser.errors)
        
        del payload['profile']
        ser = serializers.UserSerializer(instance, data=payload, partial=True)
        if ser.is_valid():
            ser.save()
        else:
            errors.extend(ser.errors)

        if errors:
            return Response({'errors': errors}, status=400)

        instance.refresh_from_db()
        return Response(serializers.UserSerializer(instance).data, status=201)
