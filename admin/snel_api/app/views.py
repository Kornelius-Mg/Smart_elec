from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .serializers import *
from user.models import *
from compteur.models import *
from transfos.models import *

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
    queryset = TransfertCredit.objects.all()
    permission_classes = (permissions.AllowAny, )

class AdresseViewsSet(viewsets.ModelViewSet):
    serializer_class = AdresseSerializer
    queryset = Adresse.objects.all()
    permission_classes = (permissions.AllowAny, )

# Home Page

class LocalLoginRequired(LoginRequiredMixin):
    login_url = '/login'

class HomeView(LocalLoginRequired, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["utilisateurs"] = Utilisateur.objects.all()
        context["Abonnements"] = Abonnement.objects.order_by("-date_heure")
        context["transferts"] = TransfertCredit.objects.order_by("-date_heure")
        context["compteurs"] = Compteur.objects.all()
        context["details"] = DetailsCompteur.objects.all()
        return context