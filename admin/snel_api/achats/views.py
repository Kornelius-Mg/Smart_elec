from django.shortcuts import render
from django.db.models import Sum, Count
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, View

from .models import Achat

from app.views import LocalLoginRequired
from compteur.models import Compteur, Classe
from parametres import reglages

# Create your views here.

class AchatsList(LocalLoginRequired, ListView):
    """
    Vue presentant la liste générale des achats
    """

    template_name = "achats.html"
    context_object_name = "achats"
    model = Achat
    queryset = Achat.objects.order_by("-instant")

    def get_context_data(self, **kwargs):
        context = super(AchatsList, self).get_context_data(**kwargs)
        context["nombre"] = self.model.objects.count()
        obj_sum = self.model.objects.aggregate(Sum('quantite'))
        context["somme_qte"] =  obj_sum['quantite__sum']
        context["len_achats"] = Achat.objects.aggregate(Count('id'))["id__count"]
        return context

class AchatCreateView(LocalLoginRequired, CreateView):
    """
        Vue d'enregistrement des achats
     """

    template_name = "new-achat.html"
    fields = ("compteur", "prix", "quantite", "classe")
    success_url = "/achats/list/"
    model = Achat
    
    def get_context_data(self, **kwargs):
        context = super(AchatCreateView, self).get_context_data(**kwargs)
        context["compteurs"] = Compteur.objects.all()
        context["prix_par_watt"] = reglages.PRIX_PAR_WATT
        context["classes"] = Classe.objects.all()
        return context

class AchatDeleteView(LocalLoginRequired, DeleteView):
    model = Achat
    template_name = "whats-up.html"
    success_url = "/achats"

class AchatUpdateView(LocalLoginRequired, UpdateView):
    template_name = "update-achat.html"
    fields = ("compteur", "prix", "quantite", "classe")
    success_url = "/achats/list"
    model = Achat
    
    def get_context_data(self, **kwargs):
        context = super(AchatUpdateView, self).get_context_data(**kwargs)
        context["compteurs"] = Compteur.objects.all()
        context["prix_par_watt"] = reglages.PRIX_PAR_WATT
        context["classes"] = Classe.objects.all()
        return context

class AchatCompteurListView(LocalLoginRequired, View):
    """
        Vue permettant d'afficher la liste des achats d'un compteur en particulier dont l'ID est representé dans le pk
    """
    def get(self, request, *args, **kwargs):
        id_compteur = kwargs["pk"]
        compteur = Compteur.objects.get(id=id_compteur)
        achats = Achat.objects.filter(compteur=compteur)
        nombre = len(achats)
        obj_sum = achats.aggregate(Sum('quantite'))
        somme_qte =  obj_sum['quantite__sum']
        url = "achat-compteur"
        return render(request, "achats.html", locals())