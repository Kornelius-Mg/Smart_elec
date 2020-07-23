from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Sum

from .models import Transfert
from .forms import TransfertForm

from app.views import LocalLoginRequired

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

class CreateTransfert(LocalLoginRequired, View):
    def get(self, request, *args, **kwargs):
        form = TransfertForm()
        compteurs = Compteur.objects.all()
        return render(request, 'new-transfert.html', locals())
    
    def post(self, request, *args, **kwargs):
        form = TransfertForm(request.POST)

        if form.is_valid():
            transfert = Transfert()
            transfert.expediteur = form.cleaned_data["expediteur"]
            transfert.destinataire = form.cleaned_data["destinataire"]
            transfert.quantite = form.cleaned_data["quantite"]

            # Verification des faisabilités du transfert
            if not self.validate_transfert(transfert.expediteur, transfert.quantite):
                error = "Erreur. le credit de l'expediteur est insuffisant pour effectuer ce transfert"
                return render(request, "new-transfert.html", locals())

            transfert.save()

            return redirect("/transferts/list/")

        else:
            return render(request, "new-transfert.html", locals())
    
    def validate_transfert(self, expediteur: Compteur, quantite: float) -> bool:
        """
            contient toutes les conditions de validation d'un transfert
        """

        if expediteur.credit <= quantite: return False

        return True

class TransfertDeleteView(LocalLoginRequired, DeleteView):
    model = Transfert
    template_name = "whats-up.html"
    success_url = "/transferts/list"

class TransfertUpdateView(LocalLoginRequired, UpdateView):
    model = Transfert
    template_name = "update-transfert.html"
    success_url = "/transferts/list"
    fields = ("expediteur", "destinataire", "quantite")
    
    def get_context_data(self, **kwargs):
        context = super(CreateTransfert, self).get_context_data(**kwargs)
        context["compteurs"] = Compteur.objects.all()
        return context