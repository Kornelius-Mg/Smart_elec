from django.db import models
from time import time

# Create your models here.

class Utilisateur(models.Model):
    """
    Model representant un utilisateur ou client de l'electricité
    """

    nom = models.CharField(max_length=45)
    postnom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    psw = models.CharField(max_length=40)
    telephone = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to="img/user/avatar/", default="img/user/avatar/avatar.jpg", unique=True)

    def save(self, *args, **kwargs):
        index = 0
        try:
            index = self.avatar.name.rindex("/")
        except ValueError:
            pass
        except Exception:
            models.FieldError()
        dossier = self.avatar.name[:index]
        fichier = self.avatar.name[index:]
        if not fichier.endswith("avatar.jpg"):
            liste_name = fichier.split(".")
            extension = liste_name[-1]
            new_name = str(time()) + "." + extension
            self.avatar.name =   new_name
            print(self.avatar.name)
        return super(Utilisateur, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s - %s"%(self.nom, self.postnom, self.prenom, self.telephone)
    
    def __unicode__(self):
        return "%s %s %s - %s"%(self.nom, self.postnom, self.prenom, self.telephone)

class Appartement(models.Model):
    """
        Model representant un appartement qui appartient à un utilisateur
    """
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
    pays = models.CharField(max_length=45, default="RDC", null=True)
    province = models.CharField(max_length=45, default="Haut-Katanga", null=True)
    ville = models.CharField(max_length=45, default="Lubumbashi", null=True)
    commune = models.CharField(max_length=45, null=True)
    quartier = models.CharField(max_length=45, null=True)
    avenue = models.CharField(max_length=45, null=True)
    numero = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return '%s %s C. %s Q. %s Av. %s N°%s'%(self.utilisateur, self.ville, self.commune, self.quartier, self.avenue, self.numero)

    def __unicode__(self):
        return '%s %s C. %s Q. %s Av. %s N°%s'%(self.utilisateur, self.ville, self.commune, self.quartier, self.avenue, self.numero)