from django.db import models
from django.contrib.auth.models import User
from time import time
import os

# Create your models here.

class Profile(models.Model):
    """
    Model qui contient les proprietés du profil de l'utilisateur
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='img/admin/avatar', default="img/admin/avatar/avatar.png")

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
        if not fichier.endswith("avatar.png"):
            liste_name = fichier.split(".")
            extension = liste_name[-1]
            new_name = str(time()) + "." + extension
            self.avatar.name =   new_name
            print(self.avatar.name)
        return super(Profile, self).save(*args, **kwargs)
