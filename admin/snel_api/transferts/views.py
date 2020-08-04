from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from django.db.models import Sum, Q

from .models import Transfert
from .forms import TransfertForm

from app.views import LocalLoginRequired
from compteur.models import Compteur

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
                compteurs = Compteur.objects.all()
                return render(request, "new-transfert.html", locals())

            transfert.save()

            return redirect("/transferts/list/")

        else:
            compteurs = Compteur.objects.all()
            return render(request, "new-transfert.html", locals())
    
    def validate_transfert(self, expediteur, quantite):
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

class TransfertsCompteurList(LocalLoginRequired, View):
    def get(self, request, *args, **kwargs):
        id_compteur = kwargs["pk"]
        compteur = Compteur.objects.get(id=id_compteur)
        transferts = Transfert.objects.filter(Q(expediteur=compteur) | Q(destinataire = compteur))
        send = transferts.filter(Q(expediteur = compteur))
        received = transferts.filter(Q(destinataire = compteur))
        len_received = len(received)
        len_send = len(send)
        obj_nbre1 = send.aggregate(Sum('quantite'))
        send_qte = obj_nbre1["quantite__sum"] or 0
        obj_nbre = received.aggregate(Sum('quantite'))
        received_qte = obj_nbre["quantite__sum"] or 0
        return render(request, "transferts.html", locals())