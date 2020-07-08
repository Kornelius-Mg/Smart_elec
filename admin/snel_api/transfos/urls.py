from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    # urls pour transfos
     path('list', TransformateurListView.as_view(), name="transfos"),
     path('new', TransformateurCreateView.as_view(), name="new-transfo"),
     url(r'^update/(?P<pk>[0-9]+)/$', TransformateurUpdateView.as_view(), name="update-transfo"),
     url(r'^delete/(?P<pk>[0-9]+)/$', TransformateurDeleteView.as_view(), name="delete-transfo"),
     url(r'^(?P<pk>[0-9]+)/$', TransformateurDetailView.as_view(), name="transfo"),
     url(r'^infos/(?P<pk>[0-9]+)/$', transformateur_infos, name="transfo-infos"),
     url(r'^start/(?P<pk>[0-9]+)/$', start_transfo, name="start-transfo"),
     url(r'^stop/(?P<pk>[0-9]+)/$', stop_transfo, name="stop-transfo"),
     
]