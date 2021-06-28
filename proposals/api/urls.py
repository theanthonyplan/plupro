from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers

from . import views as api_views

app_name = "proposals"

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'proposal', api_views.ProposalViewSet, basename='proposal')
router.register(r'proposal-line', api_views.ProposalLineViewSet, basename='proposal-line')

urlpatterns = [url(r"^", include(router.urls))]
