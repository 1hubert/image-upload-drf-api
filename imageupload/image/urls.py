"""URL mapping for the image app."""
from django.urls import (
    path,
    include
)
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('upload-image/', views.ImageView.as_view()),
]
