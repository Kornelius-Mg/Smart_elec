from django.conf.urls import url
from django.urls import path
from .views import (CompteurAppartCreateView, CompteurAppartListView, CompteurCreateView, 
                    CompteurDeleteView, CompteurListView, CompteurTransfoListView, DetailsCompteurView,
                    CompteurUpdateView, compteur_infos, start_compteur,
                    start_phase_compteur, stop_compteur, stop_phase_compteur)

urlpatterns = [
    # Urls pour compteurs
    path('list', CompteurListView.as_view(), name="compteurs"),
    path('new', CompteurCreateView.as_view(), name="new-compteur"),
    url(r'^appart/(?P<pk>[0-9]+)/$', CompteurAppartListView.as_view(), name="compteurs-appart"),
    url(r'^appart/(?P<pk>[0-9]+)/new/$', CompteurAppartCreateView.as_view(), name="new-compteur-appart"),
    url(r'^transfo/(?P<pk>[0-9]+)/$', CompteurTransfoListView.as_view(), name="compteurs-transfo"),
    url(r'^delete/(?P<pk>[0-9]+)/$', CompteurDeleteView.as_view(), name="delete-compteur"),
    url(r'^update/(?P<pk>[0-9]+)/$', CompteurUpdateView.as_view(), name="update-compteur"),
    url(r'^(?P<pk>[0-9]+)/$', DetailsCompteurView.as_view(), name="compteur"),
    url(r'^infos/(?P<pk>[0-9]+)/$', compteur_infos, name="compteur-infos"),
    url(r'^start/(?P<pk>[0-9]+)/$', start_compteur, name="start-compteur"),
    url(r'^stop/(?P<pk>[0-9]+)/$', stop_compteur, name="stop-compteur"),
    url(r'^start-phase-compteur/(?P<cpt>[0-9]+)/(?P<ph>[0-9]+)/', start_phase_compteur, name="start-phase-compteur"),
    url(r'^stop-phase-compteur/(?P<cpt>[0-9]+)/(?P<ph>[0-9]+)/', stop_phase_compteur, name="stop-phase-compteur"),

]