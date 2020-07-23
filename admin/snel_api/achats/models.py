from django.db import models
from django.db.models import F
from compteur.models import Compteur

# Create your models here.

class Achat(models.Model):
    """
    Model representant un achat de credit
    """
    instant = models.DateTimeField(auto_now=True)
    compteur = models.ForeignKey(Compteur, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=11 ,decimal_places=2)
    quantite = models.DecimalField(max_digits=11, decimal_places=2)

    def save(self, *args, **kwargs):
        
        # On incremente d'abord le credit du compteur concerné
        self.compteur.credit = F('credit') + self.quantite

        return super(Achat, self).save(*args, **kwargs)
    