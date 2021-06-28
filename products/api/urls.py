from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers

from . import views as api_views

app_name = "products"

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'product', api_views.ProductViewSet, basename='product')
router.register(r'tag', api_views.TagViewSet, basename='tag')

urlpatterns = [url(r"^", include(router.urls))]
