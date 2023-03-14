"""URL mapping for the image app."""
from django.urls import (
    path,
    include
)
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.ImageView)

urlpatterns = [
    path('', include(router.urls))
]
