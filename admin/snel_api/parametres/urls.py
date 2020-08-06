from django.urls import path
from .views import ReglagesUpdateView, ClassesUpdateView, GeneralSettingsUpdateView

urlpatterns = [
    path('', ReglagesUpdateView.as_view(), name="reglages"),
    path('general-settings', GeneralSettingsUpdateView.as_view(), name="general-settings"),
    path('classes-settings', ClassesUpdateView.as_view(), name="classes-settings"),
]
