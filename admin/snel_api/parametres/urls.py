from django.urls import path
from .views import *

urlpatterns = [
    path('', reglages, name="reglages"),
]
