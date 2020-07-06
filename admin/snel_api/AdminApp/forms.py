from django import forms
from app.models import *

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

    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=45)
    password = forms.CharField(max_length=45, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    firstname = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    username = forms.CharField(max_length=45)
    password = forms.CharField(max_length=40)
    email = forms.EmailField()
    telephone = forms.CharField(max_length=20)
