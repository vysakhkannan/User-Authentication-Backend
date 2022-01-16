from django.contrib import admin
from django.db import router
from django.urls import path, include
from . import views
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', UserViewSet, basename='users')

urlpatterns = [

    path('users/',include(router.urls))
]
