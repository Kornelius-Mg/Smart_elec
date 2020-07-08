from django import forms
from.models import *

class UtilisateurForm(forms.ModelForm):
    """Form definition for Utilisateur"""

    class Meta:
        """Meta definition for Utilisateurform."""
        model = Utilisateur
        exclude = ()

class CreateAppartForm(forms.Form):
    """CreateAppartForm definition."""
    pays = forms.CharField(max_length=45)
    province = forms.CharField(max_length=45)
    ville = forms.CharField(max_length=45)
    quartier = forms.CharField(max_length=45)
    avenue = forms.CharField(max_length=45)
    numero = forms.IntegerField(min_value=1)
