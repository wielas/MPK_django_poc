from django.urls import path

from . import views

urlpatterns = [
    path('cities/', views.cities, name='cities'),
    path('city/wroclaw/routes/', views.wroclaw_routes, name='wroclaw_routes'),
]