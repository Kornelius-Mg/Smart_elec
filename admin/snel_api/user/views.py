from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView, TemplateView, View
from app.views import LocalLoginRequired
from .models import *
from .forms import *

# Create your views here.

# Vues en rapport avec l'utilisateur
class UserCreateView(LocalLoginRequired, CreateView):
    model = Utilisateur
    template_name = "create-user.html"
    success_url = "/users/list"
    form_class = UtilisateurForm

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context["action"] = "Enregistrer"
        return context

class UserUpdateView(UpdateView):
    model = Utilisateur
    template_name = "update-user.html"
    success_url = "/users/list"
    fields = ("nom", "postnom", "prenom", "psw", "telephone")

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context["action"] = "Modifier"
        return context

class UserDeleteView(LocalLoginRequired, DeleteView):
    model = Utilisateur
    template_name = "whats-up.html"
    success_url = "/users/list"

class UserListView(LocalLoginRequired, ListView):
    model = Utilisateur
    template_name = "users.html"
    context_object_name = "users"

class UserDetailView(LocalLoginRequired, DetailView):
    model = Utilisateur
    template_name='user.html'
    context_object_name = "user"

    def get(self, request, *args, **kwargs):
        request.session["user"] = kwargs["pk"]
        return super(UserDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context["apparts"] = self.object.appartement_set.all()
        context["nb_apparts"] = self.object.appartement_set.count()
        nb = 0
        for appart in context["apparts"]:
            nb += appart.compteur_set.count()
        context["nb_compteurs"] = nb
        return context

# Vues pour adresses et appartements

class AdresseCreateView(LocalLoginRequired, CreateView):
    model = Adresse
    template_name = "create-appart.html"
    fields = ("pays", "province", "ville", "commune", "quartier", "avenue", "numero")
    success_url = "/users/apparts/new"

    def get(self, request,  *args, **kwargs):
        return super(AdresseCreateView, self).get(request, *args, **kwargs)

class AppartementCreateView(LocalLoginRequired, View):
    def get(self, request, *args, **kwargs):
        adresse = list(Adresse.objects.all())[-1]
        appart = Appartement(utilisateur=Utilisateur.objects.get(id=request.session["user"]), adresse=adresse)
        appart.save()
        return redirect("/users/%s"%request.session["user"])

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')

class AdresseDeleteView(LocalLoginRequired, DeleteView):
    model = Adresse
    template_name = "whats-up.html"

    def get(self, request, *args, **kwargs):
        AdresseDeleteView.success_url = "/users/%s"%request.session["user"]
        return super(AdresseDeleteView, self).get(request, *args, **kwargs)

class AdresseUpdateView(LocalLoginRequired, UpdateView):
    model = Adresse
    template_name = "update-appart.html"
    fields = ("pays", "province", "ville", "commune", "quartier", "avenue", "numero")
    
    def get(self, request, *args, **kwargs):
        AdresseUpdateView.success_url = "/users/" + request.session["user"]
        return super(AdresseUpdateView, self).get(request, *args, **kwargs)
