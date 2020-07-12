from django.db import models
from compteur.models import Compteur

# Create your models here.

class Achat(models.Model):
    instant = models.DateTimeField(auto_now=True)
    compteur = models.ForeignKey(Compteur, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=11 ,decimal_places=2)
    quantite = models.DecimalField(max_digits=11, decimal_places=2)
    