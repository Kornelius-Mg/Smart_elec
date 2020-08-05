from rest_framework import serializers
from superviseur.models import Profile
from compteur.models import Compteur, DetailsCompteur
from transfos.models import Transformateur
from user.models import Utilisateur, Appartement
from transferts.models import Transfert
from achats.models import Achat

    
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

class TransfertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfert
        exclude = ()

class AchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achat
        exclude = ()

class TransformateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transformateur
        exclude = ()

