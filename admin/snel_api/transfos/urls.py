from django.conf.urls import url
from django.urls import path
from .views import (TransformateurCreateView, TransfoCompteursListView, TransformateurDeleteView, 
                    TransformateurDetailView, TransformateurListView, TransformateurUpdateView, 
                    transformateur_infos, start_transfo, stop_transfo, start_phase_transfo, stop_phase_transfo)

urlpatterns = [
    # urls pour transfos
    path('list', TransformateurListView.as_view(), name="transfos"),
    path('new', TransformateurCreateView.as_view(), name="new-transfo"),
    url(r'^update/(?P<pk>[0-9]+)/$', TransformateurUpdateView.as_view(), name="update-transfo"),
    url(r'^delete/(?P<pk>[0-9]+)/$', TransformateurDeleteView.as_view(), name="delete-transfo"),
    url(r'^(?P<pk>[0-9]+)/$', TransformateurDetailView.as_view(), name="transfo"),
    url(r'^compteurs/(?P<trf>[0-9]+)/$', TransfoCompteursListView.as_view(), name="compteurs-transfo"),
    url(r'^infos/(?P<pk>[0-9]+)/$', transformateur_infos, name="transfo-infos"),
    url(r'^start/(?P<pk>[0-9]+)/$', start_transfo, name="start-transfo"),
    url(r'^stop/(?P<pk>[0-9]+)/$', stop_transfo, name="stop-transfo"),
    url(r'^phase/start/(?P<trf>[0-9]+)/(?P<ph>[0-9]+)/$', start_phase_transfo, name="start-phase-transfo"),
    url(r'^phase/stop/(?P<trf>[0-9]+)/(?P<ph>[0-9]+)/$', stop_phase_transfo, name="stop-phase-transfo"),
     
]