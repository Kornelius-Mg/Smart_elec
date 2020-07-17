from django.db import models
from compteur.models import Compteur

# Create your models here.

class Transfert(models.Model):
    instant = models.DateTimeField(auto_now=True)
    expediteur = models.ForeignKey(Compteur, on_delete=models.CASCADE, related_name="+")
    destinataire = models.ForeignKey(Compteur, on_delete = models.CASCADE, related_name="+")
    quantite = models.DecimalField(max_digits = 11, decimal_places = 2)
