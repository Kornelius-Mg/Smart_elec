from django.db import models

# Create your models here.

class ReglagesGeneral(models.Model):
    prix_par_watt = models.DecimalField(verbose_name="Prix par watt", max_digits=11, decimal_places=2)
    alert_level = models.IntegerField(verbose_name="Niveau d'alerte minimal des transfos")
    
class ClasseForfait(models.Model):
    designation = models.IntegerField(choices=((0, "Classe 1"), (1, "classe 2"), (2, "classe 3")), default=0)
    puissance_max = models.IntegerField(default=75)

    def __str__(self):
        return "%s %s"%(self.designation, self.puissance_max)