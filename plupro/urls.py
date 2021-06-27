"""plupro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from accounts.views import UserViewSet

schema_view = get_swagger_view(title='PluPro API')

urlpatterns = [
    # path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^docs', schema_view)
]

# DRF stuff
# Create a router and register our viewsets with it.

router = DefaultRouter()
router.register(r'users', UserViewSet)

# router.register(r'tags', TagViewSet)

urlpatterns += [
    path("", include(router.urls)),
    url(r"^api/", include("products.api.urls", namespace="product-api")),
]








# url routing for django-debug-toolbar
urlpatterns += [
    path('__debug__/', include(debug_toolbar.urls)),
]
