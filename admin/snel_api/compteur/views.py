from django.shortcuts import render
from django.http import HttpRequest, Http404, HttpResponse
from django.core import serializers
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView, TemplateView
from .models import *
from user.models import Appartement
from transfos.models import Transformateur
from . import compteurs_states
from app.views import LocalLoginRequired
from django.contrib.auth.decorators import login_required

# Create your views here.

# Vues concernant les compteurs
class CompteurAppartListView(LocalLoginRequired, ListView):
    model = Compteur
    template_name = "compteurs.html"
    context_object_name = "compteurs"
    
    def get(self, request, **kwargs):
        cle = kwargs["pk"]
        self.key = cle
        CompteurAppartListView.queryset = Appartement.objects.get(id=cle).compteur_set.all()
        return super(CompteurAppartListView, self).get(request, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(CompteurAppartListView, self).get_context_data(**kwargs)
        context["url"] = "compteur-appart"
        context["id_appart"] = self.key
        return context

class CompteurListView(LocalLoginRequired, ListView):
    model = Compteur
    template_name = "compteurs.html"
    context_object_name = "compteurs"
    queryset = Compteur.objects.all()


class CompteurTransfoListView(LocalLoginRequired, ListView):
    model = Compteur
    template_name = "compteurs.html"
    context_object_name = "compteurs"

class CompteurCreateView(LocalLoginRequired, CreateView):
    model = Compteur
    template_name = "create-compteur.html"
    fields = ("modele", "appartement", "transformateur", "active_class")
    success_url = "/compteurs/list/"

    def get_context_data(self, **kwargs):
        context = super(CompteurCreateView, self).get_context_data(**kwargs)
        context["apparts"] = Appartement.objects.all()
        context["transfos"] = Transformateur.objects.all()
        return context

class CompteurAppartCreateView(LocalLoginRequired, CreateView):
    model = Compteur
    template_name = "create-compteur.html"
    fields = ("modele", "appartement", "transformateur", "active_class")

    def get(self, request, **kwargs):
        self.key = kwargs["pk"]
        CompteurAppartCreateView.success_url = "/compteurs/appart/"+self.key
        return super(CompteurAppartCreateView, self).get(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CompteurAppartCreateView, self).get_context_data(**kwargs)
        context["apparts"] = Appartement.objects.all()
        context["id_appart"] = list(context["apparts"]).index(Appartement.objects.get(id=self.key)) + 1
        context["transfos"] = Transformateur.objects.all()
        return context


class DetailsCompteurView(LocalLoginRequired, DetailView):
    model = Compteur
    template_name = "compteur.html"
    context_object_name = "compteur"

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(DetailsCompteur.objects.order_by("-instant").filter(compteur=Compteur.objects.get(id=kwargs["pk"])))
            datas = json_serializer.getvalue()
            return HttpResponse(datas)
        else:
            return super(DetailsCompteurView, self).get(request, *args, **kwargs) 

    def get_context_data(self, **kwargs):
        context = super(DetailsCompteurView, self).get_context_data(**kwargs)
        context['details'] = Compteur.objects.get(id=self.object.pk).detailscompteur_set.order_by("-instant")
        return context

class CompteurDeleteView(LocalLoginRequired, DeleteView):
    model = Compteur
    template_name = "whats-up.html"
    success_url = "/compteurs/list"


class CompteurUpdateView(UpdateView):
    model = Compteur
    template_name = "update-compteur.html"
    success_url = "/compteurs/list"
    fields = ("modele", "appartement", "transformateur", "active_class")

    def get_context_data(self, **kwargs):
        context = super(CompteurUpdateView, self).get_context_data(**kwargs)
        context["apparts"] = Appartement.objects.all()
        context["id_appart"] = list(context["apparts"]).index(self.object.appartement) + 1
        context["transfos"] = Transformateur.objects.all()
        context["id_transfo"] = list(context["transfos"]).index(self.object.transformateur) + 1
        return context

# AJAX REQUESTS

def compteur_infos(request, *args, **kwargs):
    if request.is_ajax():
        JSONSerializer = serializers.get_serializer("json")
        json_serializer = JSONSerializer()
        json_serializer.serialize( Compteur.objects.filter(id=kwargs["pk"]))
        datas = json_serializer.getvalue()
        return HttpResponse(datas)


def start_compteur(request, *args, **kwargs):
    if request.method == "GET":
        responses = compteurs_states.get_infos()
        if responses:
            id_c = kwargs["pk"]
            compteur = Compteur.objects.get(id=id_c)
            compteur.global_state = "ON"
            compteur.save()
            return HttpResponse("ok")
        else:
            return Http404("Une erreur est survenue")

def stop_compteur(request, *args, **kwargs):
    if request.method == "GET":
        responses = compteurs_states.get_infos()
        if responses:
            id_c = kwargs["pk"]
            compteur = Compteur.objects.get(id=id_c)
            compteur.global_state = "OFF"
            compteur.save()
            return HttpResponse("ok")
        else:
            return Http404("Une erreur est survenue")