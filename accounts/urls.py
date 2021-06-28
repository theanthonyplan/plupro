from django.conf.urls import include
from django.conf.urls import url

from rest_framework import routers

from . import views as api_views

app_name = "accounts"

router = routers.DefaultRouter(trailing_slash=True)
router.register(r"user", api_views.UserViewSet, base_name="user")
router.register(r"user-profile", api_views.UserProfileViewSet, base_name="user-profile")

urlpatterns = [
    url(r"^current-user", api_views.current_user, name="current-user"),
    url(r"^", include(router.urls)),
]
