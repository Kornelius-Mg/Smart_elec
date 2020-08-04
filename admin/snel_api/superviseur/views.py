from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, Http404
from django.views.generic import ListView, DetailView
from superviseur.models import Profile
from .forms import RegisterAdminForm, UpdateAdminForm
from app.views import LocalLoginRequired

# Create your views here.

# AdminViews

@login_required
def register_form(request: HttpRequest, *args, **kwargs):
    print(request.method)
    if request.method == "POST":
        form = RegisterAdminForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            user = User.objects.create_user(username, email, password)
            user.first_name = form.cleaned_data["firstname"]
            user.last_name = form.cleaned_data["lastname"]
            user.save()
            profile = Profile(user=user)
            profile.telephone = form.cleaned_data["telephone"]
            if form.cleaned_data["avatar"]:
                profile.avatar = form.cleaned_data["avatar"]
            profile.save()
            user = authenticate(username=username, password=password)
            if user:
                return redirect('/superviseurs/list')
            else:
                return render(request, 'create-admin.html', {'error': 'Une erreur s\'est produite, veuillez recommencer s\'il vous plait'})
        else:
            return render(request, 'create-admin.html', locals())
    else:
        form = RegisterAdminForm()
        return render(request, 'create-admin.html', locals())

@login_required
def superviseur_update(request: HttpRequest, *args, **kwargs):
    superviseur = request.user
    if 'pk' in list(kwargs.keys()):
        superviseur = User.objects.get(username=kwargs["pk"])
    if request.method == "POST":
        form = UpdateAdminForm(request.POST, request.FILES)
        if form.is_valid():
            if form.has_changed():
                superviseur.username = form.cleaned_data["username"]
                superviseur.first_name = form.cleaned_data["firstname"]
                superviseur.last_name = form.cleaned_data["lastname"]
                superviseur.email = form.cleaned_data["email"]
                if form.cleaned_data["password"]:
                    superviseur.set_password(form.cleaned_data["password"])
                superviseur.save()
                superviseur.profile.telephone = form.cleaned_data["telephone"]
                if form.cleaned_data["avatar"]:
                    superviseur.profile.avatar = form.cleaned_data["avatar"]
                superviseur.profile.save()
            return redirect('/superviseurs/list')
        else:
            return render(request, 'update-admin.html', locals())
    else:
        form = UpdateAdminForm()
        return render(request, 'update-admin.html', locals())

@login_required
def superviseur_details(request: HttpRequest, *args, **kwargs):
    contexte = dict()
    contexte['superviseur'] = request.user
    if 'pk' in list(kwargs.keys()):
        contexte["superviseur"] = User.objects.get(username=kwargs["pk"])
    contexte['profile'] = Profile.objects.get(user=contexte["superviseur"])
    return render(request, 'admin.html', contexte)

@login_required
def delete_admin(request: HttpRequest, *args, **kwargs):
    """ Vue de suppression d'un administrateur """
    superviseur = request.user
    if 'pk' in list(kwargs.keys()):
        superviseur = User.objects.get(username=kwargs["pk"])
    if request.method == "POST":
        superviseur.delete()
        return redirect('/login')
    else:
        return render(request, 'whats-up.html', locals())

class SuperviseurList(LocalLoginRequired, ListView):
    model = User
    template_name = "admins.html"
    context_object_name = 'superviseurs'



