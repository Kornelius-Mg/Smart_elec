from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *

# Create your views here.

class AchatViewsSet(viewsets.ModelViewSet):
    serializer_class = AchatSerializer
    queryset = Achat.objects.all()
    permission_classes = (permissions.AllowAny,)

class AdministrateurViewsSet(viewsets.ModelViewSet):
    serializer_class = AdministrateurSerializer
    queryset = Administrateur.objects.all()
    permission_classes = (permissions.AllowAny, )

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
    queryset = Details_Compteur.objects.all()
    permission_classes = (permissions.AllowAny, )

class TransfertViewsSet(viewsets.ModelViewSet):
    serializer_class = TransfertSerializer
    queryset = TransfertCredit.objects.all()
    permission_classes = (permissions.AllowAny, )

class AdresseViewsSet(viewsets.ModelViewSet):
    serializer_class = AdresseSerializer
    queryset = Adresse.objects.all()
    permission_classes = (permissions.AllowAny, )