from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView, TemplateView, View
from app.views import LocalLoginRequired
from .models import Utilisateur, Appartement
from .forms import UtilisateurForm, CreateAppartForm

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
    context_object_name = "utilisateurs"

class UserDetailView(LocalLoginRequired, DetailView):
    model = Utilisateur
    template_name='user.html'
    context_object_name = "utilisateur"

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

class AppartementCreateView(LocalLoginRequired, View):
    def get(self, request,  *args, **kwargs):
        form = CreateAppartForm()
        return render(request, "create-appart.html", locals())
    
    def post(self, request, *args, **kwargs):
        form = CreateAppartForm(request.POST)
        if form.is_valid():
            appartement = Appartement()
            id_user = kwargs["pk"]
            appartement.pays = form.cleaned_data["pays"]
            appartement.province = form.cleaned_data["province"]
            appartement.ville = form.cleaned_data["ville"]
            appartement.commune = form.cleaned_data["commune"]
            appartement.quartier = form.cleaned_data["quartier"]
            appartement.avenue = form.cleaned_data["avenue"]
            appartement.numero = form.cleaned_data["numero"]
            appartement.utilisateur = Utilisateur.objects.get(id=id_user)
            appartement.save()
            return redirect('/users/'+id_user)
        else:
            return render(request, "create-appart.html", locals())
        

class AppartementDeleteView(LocalLoginRequired, DeleteView):
    model = Appartement
    template_name = "whats-up.html"

    def get(self, request, *args, **kwargs):
        AppartementDeleteView.success_url = "/users/%s"%request.session["user"]
        return super(AppartementDeleteView, self).get(request, *args, **kwargs)

class AppartementUpdateView(LocalLoginRequired, UpdateView):
    model = Appartement
    template_name = "update-appart.html"
    fields = ("pays", "province", "ville", "commune", "quartier", "avenue", "numero")
    
    def get(self, request, *args, **kwargs):
        AppartementUpdateView.success_url = "/users/" + request.session["user"]
        return super(AppartementUpdateView, self).get(request, *args, **kwargs)
