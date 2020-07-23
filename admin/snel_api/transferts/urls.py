from django.urls import path
from django.conf.urls import url
from .views import TransfertList, TransfertDeleteView, TransfertUpdateView, CreateTransfert
urlpatterns = [
    path('list', TransfertList.as_view(), name="transferts"),
    path('new', CreateTransfert.as_view(), name="new-transfert"),
    url(r'^update/(?P<pk>[0-9]+)/$', TransfertUpdateView.as_view(), name="update-transfert"),
    url(r'^delete/(?P<pk>[0-9]+)/$', TransfertDeleteView.as_view(), name="delete-transfert"),
]