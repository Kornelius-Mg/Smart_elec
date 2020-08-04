from django import forms
from.models import Utilisateur, Appartement

class UtilisateurForm(forms.Form):
    """Form definition for Utilisateur"""

    nom = forms.CharField(max_length=45)
    postnom = forms.CharField(max_length=45)
    prenom = forms.CharField(max_length=45)
    psw = forms.CharField(max_length=45)
    conf_psw = forms.CharField(max_length=45)
    telephone = forms.CharField(max_length=45)
    avatar = forms.ImageField(max_length=45)

    def clean_conf_psw(self):
        password = self.cleaned_data["password"]
        conf_psw = self.cleaned_data["conf_psw"]
        if password != conf_psw:
            raise forms.ValidationError("Les deux mots de passes doivent etre semblables")
        return conf_psw
    
    def clean_telephone(self):
        numero = self.cleaned_data["telephone"]
        pattern1 = re.compile(r'^\+243[0-9]{9}$')
        pattern2 = re.compile(r'^0[0-9]{9}$')

        if not re.fullmatch(pattern1, numero) and not re.fullmatch(pattern2, numero):
            raise forms.ValidationError("Le numero de telephone n'est pas valide")
        return numero

class CreateAppartForm(forms.Form):
    """CreateAppartForm definition."""
    pays = forms.CharField(max_length=45)
    province = forms.CharField(max_length=45)
    ville = forms.CharField(max_length=45)
    commune = forms.CharField(max_length=45)
    quartier = forms.CharField(max_length=45)
    avenue = forms.CharField(max_length=45)
    numero = forms.IntegerField(min_value=1)
