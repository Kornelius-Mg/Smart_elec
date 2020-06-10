from django.forms import ModelForm
from app.models import *

class UtilisateurForm(ModelForm):
    """Form definition for Utilisateur."""

    class Meta:
        """Meta definition for Utilisateurform."""
        model = Utilisateur
        exclude = ()
