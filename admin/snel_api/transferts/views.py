from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.db.models import Sum
from app.views import LocalLoginRequired
from .models import *

# Create your views here.

class TransfertList(LocalLoginRequired, ListView):
    template_name = "transferts.html"
    model = Transfert
    queryset = Transfert.objects.order_by("-instant")
    context_object_name = "transferts"

    def get_context_data(self, **kwargs):
        context = super(TransfertList, self).get_context_data(**kwargs)
        context["nombre"] = self.model.objects.count()
        obj_nbre = self.model.objects.aggregate(Sum('quantite'))
        context["somme_qte"] = obj_nbre["quantite__sum"] or 0
        return context

class CreateTransfert(LocalLoginRequired, CreateView):
    model = Transfert
    template_name = "new-transfert.html"
    fields = ("expediteur", "destinataire", "quantite")
    success_url = "/transferts/list/"

    def get_context_data(self, **kwargs):
        context = super(CreateTransfert, self).get_context_data(**kwargs)
        context["compteurs"] = Compteur.objects.all()
        return context