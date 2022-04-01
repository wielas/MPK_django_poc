"""MPK URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from public_transport import viewsets as views

router = routers.DefaultRouter()
router.register(r'public_transport/cities', views.CityViewSet)
router.register(r'public_transport/city/wroclaw/routes', views.RouteViewSet)
router.register(r'public_transport/city/wroclaw/stops', views.StopViewSet)
router.register(r'public_transport/city/wroclaw/trips', views.TripViewSet)
router.register(r'public_transport/city/wroclaw/stoptimes', views.StopTimesViewSet)
# router.register(r'public_transport/city/wroclaw/distance', views.DistanceViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
