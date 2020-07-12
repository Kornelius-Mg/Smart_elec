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
     url(r'^appart/new/(?P<pk>[0-9]+)/$', AppartementCreateView.as_view(), name="new-appart"),
     url(r'^apparts/update/(?P<pk>[0-9]+)/$', AppartementUpdateView.as_view(), name="update-appart"),
     url(r'^apparts/delete/(?P<pk>[0-9]+)/$', AppartementDeleteView.as_view(), name="delete-appart"),
]