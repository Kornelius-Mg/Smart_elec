from django.db import models

# Create your models here.

class ReglagesGeneral(models.Model):
    prix_par_watt = models.IntegerField(verbose_name="Prix du wattheure en francs congolais", default=100)
    min_alert_transfos = models.IntegerField(verbose_name="Niveau d'alerte minimal des transfos", default=85)
    min_alert_compteurs = models.IntegerField(verbose_name="Niveau d'alerte minimal des compteurs", default=5)