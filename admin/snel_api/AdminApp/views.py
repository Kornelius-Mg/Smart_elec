from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView, DetailView
from app.models import *
from AdminApp.forms import UtilisateurForm

# Create your views here.




class HomeView(TemplateView):
    template_name = "admin/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["utilisateurs"] = Utilisateur.objects.all()
        context["achats"] = Achat.objects.order_by("-date_heure")
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