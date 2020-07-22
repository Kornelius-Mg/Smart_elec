from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, View
from app.views import LocalLoginRequired
from parametres import reglages
from .models import *

# Create your views here.

class AchatsList(LocalLoginRequired, ListView):
    template_name = "achats.html"
    context_object_name = "achats"
    model = Achat
    queryset = Achat.objects.order_by("-instant")
    def get_context_data(self, **kwargs):
        context = super(AchatsList, self).get_context_data(**kwargs)
        context["nombre"] = self.model.objects.count()
        obj_sum = self.model.objects.aggregate(Sum('quantite'))
        context["somme_qte"] =  obj_sum['quantite__sum']
        return context

class AchatCreateView(LocalLoginRequired, CreateView):
    template_name = "new-achat.html"
    fields = ("compteur", "prix", "quantite")
    success_url = "/achats/list/"
    model = Achat
    
    def get_context_data(self, **kwargs):
        context = super(AchatCreateView, self).get_context_data(**kwargs)
        context["compteurs"] = Compteur.objects.all()
        context["prix_par_watt"] = reglages.PRIX_PAR_WATT
        return context

class AchatDeleteView(LocalLoginRequired, DeleteView):
    model = Achat
    template_name = "whats-up.html"
    success_url = "/achats"

class AchatUpdateView(LocalLoginRequired, UpdateView):
    template_name = "update-achat.html"
    fields = ("compteur", "prix", "quantite")
    success_url = "/achats/list/"
    model = Achat
    
    def get_context_data(self, **kwargs):
        context = super(AchatUpdateView, self).get_context_data(**kwargs)
        context["compteurs"] = Compteur.objects.all()
        context["prix_par_watt"] = reglages.PRIX_PAR_WATT
        return context

