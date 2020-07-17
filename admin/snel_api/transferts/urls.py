from django.urls import path
from .views import *

urlpatterns = [
    path('list', TransfertList.as_view(), name="transferts"),
    path('new', CreateTransfert.as_view(), name="new-transfert"),
]