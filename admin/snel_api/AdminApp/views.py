from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView
from app.models import *

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
    success_url = "/users/"
    fields = ('nom', 'postnom', 'prenom', 'login', 'psw', 'telephone')


class UserUpdateView(UpdateView):
    model = Utilisateur
    template_name = "admin/create-user.html"
    success_url = "/users/"

class UserDeleteView(DeleteView):
    model = Utilisateur
    template_name = "whats-up.html"
    success_url = "/users/"

class UserListView(ListView):
    model = Utilisateur
    template_name = "admin/users.html"
    context_object_name = "users"

