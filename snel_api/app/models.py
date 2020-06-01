from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    nom = models.CharField(max_length=45)
    postnom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    login = models.CharField(max_length=45)
    psw = models.CharField(max_length=40)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s %s - %s"%(self.nom, self.postnom, self.prenom, self.telephone)
    
    def __unicode__(self):
        return "%s %s %s - %s"%(self.nom, self.postnom, self.prenom, self.telephone)

class Administrateur(Utilisateur):
    email = models.CharField(max_length=45)

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
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.DO_NOTHING)
    id_adresse = models.OneToOneField(Adresse, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s'%(self.id_utilisateur, self.id_adresse)

    def __unicode__(self):
        return '%s %s'%(self.id_utilisateur, self.id_adresse)

class Compteur(models.Model):
    id_appart = models.ForeignKey(Appartement, on_delete=models.DO_NOTHING)
    modele = models.CharField(max_length=45)

    def __str__(self):
        return '%s %s'%(self.id_appart, self.modele)

    def __unicode__(self):
        return '%s %s'%(self.id_appart, self.modele)

class Details_Compteur(models.Model):
    id_compteur = models.ForeignKey(Compteur, on_delete=models.DO_NOTHING)
    credit = models.FloatField()
    instant = models.DateTimeField(auto_now=True)
    i_phase1 = models.FloatField()
    i_phase2 = models.FloatField()
    i_phase3 = models.FloatField()
    u_phase1 = models.FloatField()
    u_phase2 = models.FloatField()
    u_phase3 = models.FloatField()
    p_phase1 = models.FloatField()
    p_phase2 = models.FloatField()
    p_phase3 = models.FloatField()
    q_phase1 = models.FloatField()
    q_phase2 = models.FloatField()
    q_phase3 = models.FloatField()
    etat = models.CharField(max_length=45)

class Achat(models.Model):
    date_heure = models.DateTimeField(verbose_name="Date et heure de l'achat", auto_now=True)
    id_compteur = models.ForeignKey(Compteur, on_delete=models.DO_NOTHING)
    montant = models.FloatField()
    qte_energie = models.FloatField()
 
class TransfertCredit(models.Model):
    idExp = models.ForeignKey(Compteur, on_delete=models.DO_NOTHING, related_name="expediteur")
    idDest = models.ForeignKey(Compteur, on_delete=models.DO_NOTHING, related_name="destinataire")
    date_heure = models.DateTimeField(verbose_name="Date et heure du transfert", auto_now=True)
    qteTransfert = models.FloatField()

    def __str__(self):
        return 

    def __unicode__(self):
        return 
 
