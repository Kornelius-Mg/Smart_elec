from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView, DetailView, FormView, View
from app.models import *
from AdminApp.forms import UtilisateurForm, CreateAppartForm

# Create your views here.




class HomeView(TemplateView):
    template_name = "admin/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["utilisateurs"] = Utilisateur.objects.all()
        context["Abonnements"] = Abonnement.objects.order_by("-date_heure")
        context["transferts"] = TransfertCredit.objects.order_by("-date_heure")
        context["compteurs"] = Compteur.objects.all()
        context["details"] = Details_Compteur.objects.all()
        return context


# Vues en rapport avec l'utilisateur

class UserCreateView(CreateView):
    model = Utilisateur
    template_name = "admin/create-user.html"
    success_url = "/admin-snel/users/"
    form_class = UtilisateurForm

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context["action"] = "Enregistrer"
        return context


class UserUpdateView(UpdateView):
    model = Utilisateur
    template_name = "admin/update-user.html"
    success_url = "/admin-snel/users/"
    fields = ("nom", "postnom", "prenom", "psw", "telephone")

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context["action"] = "Modifier"
        return context

class UserDeleteView(DeleteView):
    model = Utilisateur
    template_name = "whats-up.html"
    success_url = "/admin-snel/users/"

class UserListView(ListView):
    model = Utilisateur
    template_name = "admin/users.html"
    context_object_name = "users"

class UserDetailView(DetailView):
    model = Utilisateur
    template_name='admin/user.html'
    context_object_name = "user"

    def get(self, request, *args, **kwargs):
        request.session["user"] = kwargs["pk"]
        return super(UserDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context["apparts"] = self.object.appartement_set.all()
        context["nb_apparts"] = len(context["apparts"])
        return context


# Vues pour adresses et appartements


class AdresseCreateView(CreateView):
    model = Adresse
    template_name = "admin/create-appart.html"
    fields = ("pays", "province", "ville", "commune", "quartier", "avenue", "numero")
    success_url = "/admin-snel/apparts/new"

    def get(self, request,  *args, **kwargs):
        return super(AdresseCreateView, self).get(request, *args, **kwargs)

class AppartementCreateView(View):
    def get(self, request, *args, **kwargs):
        adresse = list(Adresse.objects.all())[-1]
        appart = Appartement(utilisateur=Utilisateur.objects.get(id=request.session["user"]), adresse=adresse)
        appart.save()
        return redirect("/admin-snel/user/%s"%request.session["user"])

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')

class AdresseDeleteView(DeleteView):
    model = Adresse
    template_name = "whats-up.html"

    def get(self, request, *args, **kwargs):
        AdresseDeleteView.success_url = "/admin-snel/user/%s"%request.session["user"]
        return super(AdresseDeleteView, self).get(request, *args, **kwargs)

class AdresseUpdateView(UpdateView):
    model = Adresse
    template_name = "admin/update-appart.html"
    fields = ("pays", "province", "ville", "commune", "quartier", "avenue", "numero")
    
    def get(self, request, *args, **kwargs):
        AdresseUpdateView.success_url = "/admin-snel/user/" + request.session["user"]
        return super(AdresseUpdateView, self).get(request, *args, **kwargs)


# Vues concernant les compteurs


class CompteurListView(ListView):
    model = Compteur
    template_name = "admin/compteurs.html"
    context_object_name = "compteurs"
    
    def get(self, request, **kwargs):
        cle = kwargs["pk"]
        CompteurListView.queryset = Appartement.objects.get(id=cle).compteur_set.all()
        return super(CompteurListView, self).get(request, **kwargs)



# Vues concernant les transformateurs


class TransformateurListView(ListView):
    model = Transformateur
    template_name = "admin/transfos.html"
    context_object_name = "transfos"


class TransformateurDetailView(DetailView):
    model = Transformateur
    template_name = "admin/transfo.html"
    context_object_name = "transfo"

    def get_context_data(self, **kwargs):
        context = super(TransformateurDetailView, self).get_context_data(**kwargs)
        context['transfos'] = Transformateur.get(id=self.object.pk).compteur_set.all()
        return context










