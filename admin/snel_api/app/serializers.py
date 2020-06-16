from rest_framework import serializers
from .models import *


class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        exclude = ()
    
class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        exclude = ()
    
class AppartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appartement
        exclude = ()

class CompteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compteur
        exclude = ()

class DetailsCompteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsCompteur
        exclude = ()

class TransfertSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransfertCredit
        exclude = ()

class AdresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        exclude =()