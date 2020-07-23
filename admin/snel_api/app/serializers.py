from rest_framework import serializers
from superviseur.models import Profile
from compteur.models import Compteur, Abonnement, DetailsCompteur
from transfos.models import Transformateur
from user.models import Utilisateur, Appartement
from transferts.models import Transfert



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
        model = Transfert
        exclude = ()