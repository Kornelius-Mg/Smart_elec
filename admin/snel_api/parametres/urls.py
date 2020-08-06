from django.urls import path
from .views import ReglagesUpdateView

urlpatterns = [
    path('', ReglagesUpdateView.as_view(), name="reglages"),
]
