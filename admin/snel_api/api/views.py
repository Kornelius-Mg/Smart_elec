from rest_framework import viewsets
from rest_framework import permissions

from .serializers import (UtilisateurSerializer, AppartementSerializer, CompteurSerializer,
                         TransfertSerializer, AchatSerializer, TransformateurSerializer)

from user.models import Utilisateur, Appartement
from compteur.models import Compteur, Classe
from achats.models import Achat
from transferts.models import Transfert
from transfos.models import Transformateur

# REST APIS

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

class TransfertViewsSet(viewsets.ModelViewSet):
    serializer_class = TransfertSerializer
    queryset = Transfert.objects.all()
    permission_classes = (permissions.AllowAny, )

class TransformateurViewsSet(viewsets.ModelViewSet):
    serializer_class = TransformateurSerializer
    queryset = Transformateur.objects.all()
    permission_classes = (permissions.AllowAny, )

class AchatViewsSet(viewsets.ModelViewSet):
    serializer_class = AchatSerializer
    queryset = Achat.objects.all()
    permission_classes = (permissions.AllowAny, )