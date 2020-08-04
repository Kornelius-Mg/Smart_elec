from django.db import models
from django.db.models import F
from app.models import Detail
from transfos.models import Transformateur
from user.models import Appartement

# Create your models here.

class Classe(models.Model):
    """
    Model qui represente une classe du compteur
    """
    designation = models.CharField(max_length=45, choices=(("Domestique", "Domestique"), ("Semi-industriel", "Semi-industriel"), ("Industriel", "Industriel")))
    p_max = models.FloatField()
    q_max = models.FloatField()

    def __str__(self):
        return "%s - %.2f"%(self.designation, self.p_max)

class Compteur(models.Model):
    """
    Model qui represente un compteur électrique
    """
    modele = models.IntegerField(choices=(("Monophasé", "Monophasé"), ("Biphasé", "Biphasé"), ("Triphasé", "Triphasé")))
    credit = models.FloatField(default=0)
    transformateur = models.ForeignKey(Transformateur, on_delete=models.SET_NULL, null=True, default=None)
    appartement = models.ForeignKey(Appartement, on_delete=models.SET_NULL, null=True)
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True)

    p_total = models.FloatField(default=0)
    q_total = models.FloatField(default=0)

    i_phase1 = models.FloatField(default=0)
    i_phase2 = models.FloatField(default=0)
    i_phase3 = models.FloatField(default=0)

    u_phase1 = models.FloatField(default=0)
    u_phase2 = models.FloatField(default=0)
    u_phase3 = models.FloatField(default=0)

    p_phase1 = models.FloatField(default=0)
    p_phase2 = models.FloatField(default=0)
    p_phase3 = models.FloatField(default=0)

    q_phase1 = models.FloatField(default=0)
    q_phase2 = models.FloatField(default=0)
    q_phase3 = models.FloatField(default=0)

    global_state = models.CharField(max_length=10, choices=(("OFF", "Eteint"), ("ON", "Allumé")), default="OFF")
    phase1_state = models.CharField(max_length=10, choices=(("OFF", "Eteint"), ("ON", "Allumé")), default="OFF")
    phase2_state = models.CharField(max_length=10, choices=(("OFF", "Eteint"), ("ON", "Allumé")), default="OFF")
    phase3_state = models.CharField(max_length=10, choices=(("OFF", "Eteint"), ("ON", "Allumé")), default="OFF")

    def __str__(self):
        return '%s %s'%(self.appartement, self.modele)

    def __unicode__(self):
        return '%s %s'%(self.appartement, self.modele)


class DetailsCompteur(Detail):
    compteur = models.ForeignKey(Compteur, on_delete=models.CASCADE)

    def save(self):
        self.p_total = self.p_phase1 + self.p_phase2 + self.p_phase3
        self.q_total = self.q_phase1 + self.q_phase2 + self.q_phase3

        self.compteur.p_total = F('p_total') + self.p_total
        self.compteur.q_total = F('q_total') + self.q_total

        self.compteur.p_phase1 = F('p_phase1') + self.p_phase1
        self.compteur.p_phase2 = F('p_phase2') + self.p_phase2
        self.compteur.p_phase3 = F('p_phase3') + self.p_phase3

        self.compteur.q_phase1 = F('q_phase1') + self.q_phase1
        self.compteur.q_phase2 = F('q_phase2') + self.q_phase2
        self.compteur.q_phase3 = F('q_phase3') + self.q_phase3

        self.compteur.u_phase1 = F('u_phase1') + self.u_phase1
        self.compteur.u_phase2 = F('u_phase2') + self.u_phase2
        self.compteur.u_phase3 = F('u_phase3') + self.u_phase3

        self.compteur.i_phase1 = F('i_phase1') + self.i_phase1
        self.compteur.i_phase2 = F('i_phase1') + self.i_phase2
        self.compteur.i_phase3 = F('i_phase1') + self.i_phase3

        self.compteur.global_state = "ON"

        self.compteur.save()

        return super(DetailsCompteur, self).save()