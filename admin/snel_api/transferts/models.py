from django.db import models
from django.db.models import F
from compteur.models import Compteur

# Create your models here.

class Transfert(models.Model):
    """
    Model qui represente le transfert de credit entre deux compteurs
    """
    instant = models.DateTimeField(auto_now=True)
    expediteur = models.ForeignKey(Compteur, on_delete=models.CASCADE, related_name="+")
    destinataire = models.ForeignKey(Compteur, on_delete = models.CASCADE, related_name="+")
    quantite = models.DecimalField(max_digits = 11, decimal_places = 2)

    def save(self, *args, **kwargs):
        # On soustrait d'abord la quantité du transfert à l'expediteur
        self.expediteur.credit = F('credit') - self.quantite

        # on l'ajoute au destinataire
        self.destinataire.credit = F('credit') + self.quantite

        return super(Transfert, self).save(*args, **kwargs)
