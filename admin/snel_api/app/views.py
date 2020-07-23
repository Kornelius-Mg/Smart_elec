from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import (AbonnementSerializer, UtilisateurSerializer,
                        AppartementSerializer, CompteurSerializer,
                        TransfertSerializer, DetailsCompteurSerializer)

from compteur.models import Compteur, DetailsCompteur, Abonnement
from transfos.models import Transformateur
from user.models import Utilisateur, Appartement
from transferts.models import Transfert

# Create your views here.


# REST APIS

class AbonnementViewsSet(viewsets.ModelViewSet):
    serializer_class = AbonnementSerializer
    queryset = Abonnement.objects.all()
    permission_classes = (permissions.AllowAny,)

class UtilisateurViewsSet(viewsets.ModelViewSet):
    serializer_class = UtilisateurSerializer
    queryset = Utilisateur.objects.all()
    permission_classes = (permissions.AllowAny, )

class AppartementViewsSet(viewsets.ModelViewSet):
    serializer_class = AppartementSerializer
    queryset = Appartement.objects.all()
    permission_classes = (permissions.AllowAny, )

class CompteurViewsSet(viewsets.ModelViewSet):
    serializer_class = AppartementSerializer
    queryset = Compteur.objects.all()
    permission_classes = (permissions.AllowAny, )

class DetailsCompteurViewsSet(viewsets.ModelViewSet):
    serializer_class = DetailsCompteurSerializer
    queryset = DetailsCompteur.objects.all()
    permission_classes = (permissions.AllowAny, )

class TransfertViewsSet(viewsets.ModelViewSet):
    serializer_class = TransfertSerializer
    queryset = Transfert.objects.all()
    permission_classes = (permissions.AllowAny, )

# Home Page

class LocalLoginRequired(LoginRequiredMixin):
    """
        Classe locale obligeant l'authentification des utilisateurs pour
        exploiter une vue
    """
    login_url = '/login'

class HomeView(LocalLoginRequired, TemplateView):
    """
        Page d'accueil du site
    """
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["utilisateurs"] = Utilisateur.objects.all()
        context["Abonnements"] = Abonnement.objects.order_by("-date_heure")
        context["transferts"] = Transfert.objects.order_by("-date_heure")
        context["compteurs"] = Compteur.objects.all()
        context["details"] = DetailsCompteur.objects.all()
        return context