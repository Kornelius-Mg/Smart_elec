from django.db import models
from django.db.models import F
from app.models import Detail

# Create your models here.

class Transformateur(models.Model):
    """
        Model representant un transformateur électrique
    """
    designation = models.CharField(max_length=45)

    p_max = models.FloatField()
    q_max = models.FloatField()

    p_total = models.FloatField(default=0)
    q_total = models.FloatField(default=0)

    global_state = models.CharField(max_length=10, choices = (("OFF",'OFF'), ("ON", "ON")), default="OFF")

    def __str__(self):
        return "%s %.2f KVA"%(self.designation, self.p_max)


class DetailsTransfo(Detail):
    """
        Model representatnt les details instantanés des transfos
    """

    transformateur = models.ForeignKey(Transformateur, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.p_total = self.p_phase1 + self.p_phase2 + self.p_phase3
        self.q_total = self.q_phase1 + self.q_phase2 + self.q_phase3

        self.transformateur.p_total = F('p_total') + self.p_total
        self.transformateur.q_total = F('q_total') + self.q_total

        self.transformateur.global_state = "ON"

        self.transformateur.save()

        return super(DetailsTransfo, self).save(*args, **kwargs)
