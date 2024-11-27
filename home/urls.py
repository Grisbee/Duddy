from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage_url"),
    path("base/", views.test, name="base_url"),
    path("map/", views.map_page, name="map_url"),
]
