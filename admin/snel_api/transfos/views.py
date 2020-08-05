from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.db.models import Sum
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView, TemplateView, View
from .models import Transformateur, DetailsTransfo
from app.views import LocalLoginRequired
from . import transfos_states

# Create your views here.

class TransformateurListView(LocalLoginRequired, ListView):
    model = Transformateur
    template_name = "transfos.html"
    context_object_name = "transfos"


class TransformateurDetailView(LocalLoginRequired, DetailView):
    model = Transformateur
    template_name = "transfo.html"
    context_object_name = "transfo"

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(DetailsTransfo.objects.order_by("-instant").filter(transformateur=Transformateur.objects.get(id=kwargs["pk"])))
            datas = json_serializer.getvalue()
            return HttpResponse(datas)
        else:
            return super(TransformateurDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TransformateurDetailView, self).get_context_data(**kwargs)
        context['compteurs'] = Transformateur.objects.get(id=self.object.pk).compteur_set.all()
        context['details'] = Transformateur.objects.get(id=self.object.pk).detailstransfo_set.order_by("-instant")
        context["nb_compteurs"] = len(context['compteurs'])
        puissance_totale = 0
        for compteur in context['compteurs']:
            puissance_totale += compteur.classe.p_max
        context["charge_rate"] = puissance_totale * 100 / self.object.p_max
        return context

class TransformateurCreateView(LocalLoginRequired, CreateView):
    model = Transformateur
    template_name = "create-transfo.html"
    success_url = "/transfos/list"
    fields = ("designation", "p_max", "q_max")


class TransformateurUpdateView(LocalLoginRequired, UpdateView):
    model = Transformateur
    template_name = "update-transfo.html"
    fields = ("designation", "p_max", "q_max")
    success_url = "/transfos/list"


class TransformateurDeleteView(LocalLoginRequired, DeleteView):
    model = Transformateur
    template_name = "whats-up.html"
    success_url = "/transfos/list"

class TransfoCompteursListView(LocalLoginRequired, View):
    """
    Une vue permettant d'afficher les compteurs branchés sur un transformateur
    """
    def get(self, request, *args, **kwargs):
        id_transfo = kwargs["trf"]
        transfo = Transformateur.objects.get(id=id_transfo)
        compteurs = transfo.compteur_set.all()
        return render(request, "compteurs.html", locals())

# AJAX REQUESTS

@login_required
def transformateur_infos(request, *args, **kwargs):
    """
    Vue visant à ramener les infos globales d'un transformateur
    """
    if request.is_ajax():
        JSONSerializer = serializers.get_serializer("json")
        json_serializer = JSONSerializer()
        json_serializer.serialize(Transformateur.objects.filter(id=kwargs["pk"]))
        datas = json_serializer.getvalue()
        return HttpResponse(datas)

@login_required
def start_transfo(request, *args, **kwargs):
    """
    Vue permettant de demarrer un transfo à distance
    """
    if request.method == "GET":
        responses = transfos_states.get_infos()
        if responses:
            id_t = kwargs["pk"]
            transfo = Transformateur.objects.get(id=id_t)
            transfo.global_state = "ON"
            transfo.save()
            return HttpResponse("ok")
        else:
            return Http404("Une erreur est survenue")

@login_required
def stop_transfo(request, *args, **kwargs):
    """
    Vue permettant d'arreter un transfo à distance
    """
    if request.method == "GET":
        responses = transfos_states.get_infos()
        if responses:
            id_t = kwargs["pk"]
            transfo = Transformateur.objects.get(id=id_t)
            transfo.global_state = "OFF"
            transfo.save()
            return HttpResponse("ok")
        else:
            return Http404("Une erreur est survenue")
