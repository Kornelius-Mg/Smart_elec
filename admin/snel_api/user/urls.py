from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    # URLS pour utilisateurs
     path('new', UserCreateView.as_view(), name="new-user"),
     path('list', UserListView.as_view(), name="users"),
     url(r'^delete/(?P<pk>[0-9]+)/$', UserDeleteView.as_view(), name="delete-user"),
     url(r'^update/(?P<pk>[0-9]+)/$', UserUpdateView.as_view(), name="update-user"),
     url(r'^(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name="user"),
     
    # URLS pour appartements et adresses
     url(r'^adresses/new/(?P<pk>[0-9]+)/$', AdresseCreateView.as_view(), name="new-adresse"),
     url(r'^apparts/update/(?P<pk>[0-9]+)/$', AdresseUpdateView.as_view(), name="update-appart"),
     url(r'^apparts/delete/(?P<pk>[0-9]+)/$', AdresseDeleteView.as_view(), name="delete-appart"),
     url(r'^apparts/new/$', AppartementCreateView.as_view(), name="new-appart"),
]