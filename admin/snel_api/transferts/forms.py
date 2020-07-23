from django import forms
    
class TransfertForm(forms.ModelForm):
    class Meta:
        excludes = ('instant')
    
    def clean_destinataire(self):
        destinataire = self.cleaned_data["destinataire"]
        expediteur = self.cleaned_data["expediteur"]

        if destinataire == expediteur:
            raise forms.ValidationError("Le destinataire doit etre different de l'expediteur")
        return destinataire
    
    def clean_quantite(self):
        quantite = self.cleaned_data["quantite"]

        if quantite <= 0:
            raise forms.ValidationError("La quantité de transfert doit etre un montant strictement positif")
        return quantite

    