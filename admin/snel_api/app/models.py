from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    nom = models.CharField(max_length=45)
    postnom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    psw = models.CharField(max_length=40)
    telephone = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to="medias/img/", default="medias/img/avatar.jpg")

    def __str__(self):
        return "%s %s %s - %s"%(self.nom, self.postnom, self.prenom, self.telephone)
    
    def __unicode__(self):
        return "%s %s %s - %s"%(self.nom, self.postnom, self.prenom, self.telephone)

class Adresse(models.Model):
    pays = models.CharField(max_length=45, default="RDC")
    province = models.CharField(max_length=45, default="Haut-Katanga")
    ville = models.CharField(max_length=45, default="Lubumbashi")
    commune = models.CharField(max_length=45)
    quartier = models.CharField(max_length=45)
    avenue = models.CharField(max_length=45)
    numero = models.PositiveIntegerField()

    def __str__(self):
        return "%s C. %s Q. %s Av. %s  N°%s"%(self.ville, self.commune, self.quartier, self.avenue, self.numero)

    def __unicode__(self):
        return "%s C. %s Q. %s Av. %s  N°%s"%(self.ville, self.commune, self.quartier, self.avenue, self.numero) 

class Appartement(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.DO_NOTHING)
    adresse = models.OneToOneField(Adresse, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s'%(self.utilisateur, self.adresse)

    def __unicode__(self):
        return '%s %s'%(self.utilisateur, self.adresse)

class Classes(models.Model):
    designation = models.IntegerField(choices=((0, "CLASSE 1"), (1, "CLASSE 2"), (3, "CLASSE 3")))
    p_max = models.FloatField()
    q_max = models.FloatField()

    def __str__(self):
        return "%s - %.2f"%(self.designation, self.puissance_max)

class Transformateur(models.Model):
    designation = models.CharField(max_length=45)
    p_max = models.FloatField()
    q_max = models.FloatField()
    p_total = models.FloatField(default=0)
    q_total = models.FloatField(default=0)
    global_state = models.CharField(max_length=10, choices = (("OFF",'OFF'), ("ON", "ON")), default="OFF")

    def __str__(self):
        return "%s %.2f KVA"%(self.designation, self.p_max)

class Compteur(models.Model):
    modele = models.IntegerField(choices=((0, "Monophasé"), (1, "Biphasé"), (2, "Triphasé")))
    credit = models.FloatField(default=0)
    transformateur = models.ForeignKey(Transformateur, on_delete=models.DO_NOTHING, null=True, default=None)
    appartement = models.ForeignKey(Appartement, on_delete=models.DO_NOTHING)
    active_class = models.IntegerField(choices = ((0, "Domestique"), (1, "Semi-industriel"), (2, "Industriel")), default=0)
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

    def __str__(self):
        return '%s %s'%(self.appartement, self.modele)

    def __unicode__(self):
        return '%s %s'%(self.appartement, self.modele)

class Balance(models.Model):
    balance1 = models.FloatField()
    balance2 = models.FloatField()
    balance3 = models.FloatField()
    compteur = models.OneToOneField(Compteur, on_delete=models.CASCADE)

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

class DetailsCompteur(Detail):
    compteur = models.ForeignKey(Compteur, on_delete=models.CASCADE)

    def save(self):
        self.p_total = self.p_phase1 + self.p_phase2 + self.p_phase3
        self.q_total = self.q_phase1 + self.q_phase2 + self.q_phase3
        self.compteur.p_total += self.p_total
        self.compteur.q_total += self.q_total
        self.compteur.p_phase1 += self.p_phase1
        self.compteur.p_phase2 += self.p_phase2
        self.compteur.p_phase3 += self.p_phase3
        self.compteur.q_phase1 += self.q_phase1
        self.compteur.q_phase2 += self.q_phase2
        self.compteur.q_phase3 += self.q_phase3
        self.compteur.u_phase1 += self.u_phase1
        self.compteur.u_phase2 += self.u_phase2
        self.compteur.u_phase3 += self.u_phase3
        self.compteur.i_phase1 += self.i_phase1
        self.compteur.i_phase2 += self.i_phase2
        self.compteur.i_phase3 += self.i_phase3
        self.compteur.global_state = "ON"
        self.compteur.save()
        return super(DetailsCompteur, self).save()
        

class Abonnement(models.Model):
    date_heure = models.DateTimeField(verbose_name="Date et heure de l'Abonnement", auto_now=True)
    compteur = models.ForeignKey(Compteur, on_delete=models.DO_NOTHING)
    montant = models.FloatField()
    classe = models.ForeignKey(Classes, on_delete=models.DO_NOTHING)
    qte_energie = models.FloatField()
    etat = models.IntegerField(choices=((0, "En cours"), (1, "Terminé")))
 
class TransfertCredit(models.Model):
    expeditaire = models.ForeignKey(Compteur, on_delete=models.DO_NOTHING, related_name="expediteur")
    destinataire = models.ForeignKey(Compteur, on_delete=models.DO_NOTHING, related_name="destinataire")
    date_heure = models.DateTimeField(verbose_name="Date et heure du transfert", auto_now=True)
    qteTransfert = models.FloatField()

    def __str__(self):
        return "%s >> %s %s %s"%(self.expeditaire, self.destinataire, self.qteTransfert, self.date_heure)


class DetailsTransfo(Detail):
    transformateur = models.ForeignKey(Transformateur, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.p_total = self.p_phase1 + self.p_phase2 + self.p_phase3
        self.q_total = self.q_phase1 + self.q_phase2 + self.q_phase3
        self.transformateur.p_total += self.p_total
        self.transformateur.q_total += self.q_total
        self.transformateur.global_state = "ON"
        self.transformateur.save()
        return super(DetailsTransfo, self).save(*args, **kwargs)
