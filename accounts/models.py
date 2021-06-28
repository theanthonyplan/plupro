# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# # Create your models here.
# class ActiveManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    is_client = models.BooleanField(default=False)
    title = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	# objects = ActiveManager()

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
