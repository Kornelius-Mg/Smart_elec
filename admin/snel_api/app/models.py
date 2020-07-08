from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Detail(models.Model):
    class Meta:
        abstract = True
    instant = models.DateTimeField(auto_now=True)
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
    p_total = models.FloatField(default=0)
    q_total = models.FloatField(default=0)
    etat = models.CharField(max_length=45)