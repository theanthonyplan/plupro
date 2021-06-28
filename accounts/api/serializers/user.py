from rest_framework import serializers

from django.contrib.auth.models import User
from .user_profile import UserProfileSerializer

class UserSerializer(serializers.ModelSerializer):

    profile = UserProfileSerializer(source='userprofile', read_only=False)

    class Meta:
        model = User
        fields = "__all__"

    def update(self, instance, validated_data):
        profile = validated_data['profile']
        userprofile = UserProfileSerializer(instance.userprofile, profile, partial=True)

        errors = []
        if userprofile.is_valid():
            userprofile.save()
        else:
            errors.append()


        instance.some_field = validated_data['profile']
        instance.save()

        # Delete any detail not included in the request
        owner_ids = [item['owner_id'] for item in validated_data['owners']]
        for owner in cars.owners.all():
            if owner.id not in owner_ids:
                owner.delete()

        # Create or update owner
        for owner in validated_data['owners']:
            ownerObj = Owner.objects.get(pk=item['id'])
            if ownerObje:
                ownerObj.some_field=item['some_field']
                # ....fields...
            else:
               ownerObj = Owner.create(car=instance,**owner)
            ownerObj.save()

        return instance
