from django.shortcuts import render
from django.views.generic import ListView, CreateView
from app.views import LocalLoginRequired
from parametres import reglages
from .models import *

# Create your views here.

class AchatsList(LocalLoginRequired, ListView):
    template_name = "achats.html"
    context_object_name = "achats"
    model = Achat

class AchatCreateView(LocalLoginRequired, CreateView):
    template_name = "new-achat.html"
    fields = ("compteur", "prix", "quantite")
    success_url = "/achats/"
    model = Achat
    
    def get_context_data(self, **kwargs):
        context = super(AchatCreateView, self).get_context_data(**kwargs)
        context["compteurs"] = Compteur.objects.all()
        context["prix_par_watt"] = reglages.PRIX_PAR_WATT
        return context
