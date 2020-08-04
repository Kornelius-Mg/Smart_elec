from django.db import models
from django.db.models import F
from compteur.models import Compteur, Classe

# Create your models here.

class Achat(models.Model):
    """
    Model representant un achat de credit
    """
    instant = models.DateTimeField(auto_now=True)
    compteur = models.ForeignKey(Compteur, on_delete=models.CASCADE)
    prix = models.FloatField()
    quantite = models.FloatField()
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        
        # On incremente d'abord le credit du compteur concerné
        self.compteur.credit += self.quantite
        self.compteur.classe = self.classe
        self.compteur.save()

        return super(Achat, self).save(*args, **kwargs)
    