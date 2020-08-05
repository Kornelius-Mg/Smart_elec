from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from compteur.models import Compteur, DetailsCompteur
from transfos.models import Transformateur
from user.models import Utilisateur, Appartement
from transferts.models import Transfert

# Home Page

class LocalLoginRequired(LoginRequiredMixin):
    """
        Classe locale obligeant l'authentification des utilisateurs pour
        exploiter une vue
    """
    login_url = '/login'

class HomeView(LocalLoginRequired, TemplateView):
    """
        Page d'accueil du site
    """
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["utilisateurs"] = Utilisateur.objects.all()
        context["transferts"] = Transfert.objects.order_by("-date_heure")
        context["compteurs"] = Compteur.objects.all()
        context["details"] = DetailsCompteur.objects.all()
        return context