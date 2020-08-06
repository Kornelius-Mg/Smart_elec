from django import forms

class SettingsForm(forms.Form):
    prix_par_watt = forms.IntegerField(min_value=0)
    min_alert_transfos = forms.IntegerField(min_value=0, max_value=100)
    min_alert_compteurs = forms.IntegerField(min_value=0, max_value=100)
    
