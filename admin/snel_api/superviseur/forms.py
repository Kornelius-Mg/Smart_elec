from django import forms
import re

class LoginForm(forms.Form):
    username = forms.CharField(max_length=45)
    password = forms.CharField(max_length=45, widget=forms.PasswordInput)

class RegisterAdminForm(forms.Form):
    error_css_class = 'form-error'
    required_css_class ='form-control'
    firstname = forms.CharField(max_length=45)
    lastname = forms.CharField(max_length=45)
    username = forms.CharField(max_length=45)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)
    conf_psw = forms.CharField(max_length=40, widget=forms.PasswordInput)
    email = forms.EmailField()
    telephone = forms.CharField(max_length=20)
    avatar = forms.ImageField(required=False)

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

class UpdateAdminForm(RegisterAdminForm):
    password = forms.CharField(max_length=40, required=False, widget=forms.PasswordInput)
    conf_psw = forms.CharField(max_length=40, required=False, widget=forms.PasswordInput)
