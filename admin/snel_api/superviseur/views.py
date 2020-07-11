from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, Http404
from django.views.generic import ListView, DetailView
from superviseur.models import Profile
from .forms import *
from app.views import LocalLoginRequired
from superviseur.forms import RegisterAdminForm

# Create your views here.

# AdminViews

def login_admin(request, *args, **kwargs):
    return HttpResponse("ok")

@login_required
def register_admin(request, *args, **kwargs):
    return HttpResponse("ok")

@login_required
def logout_admin(request, *args, **kwargs):
    return HttpResponse("ok")

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
    if request.method == "POST":
        form = UpdateAdminForm(request.POST, request.FILES)
        if form.is_valid():
            if form.has_changed():
                request.user.username = form.cleaned_data["username"]
                request.user.first_name = form.cleaned_data["firstname"]
                request.user.last_name = form.cleaned_data["lastname"]
                request.user.email = form.cleaned_data["email"]
                if form.cleaned_data["password"]:
                    request.user.set_password(form.cleaned_data["password"])
                request.user.save()
                request.user.profile.telephone = form.cleaned_data["telephone"]
                if form.cleaned_data["avatar"]:
                    request.user.profile.avatar = form.cleaned_data["avatar"]
                request.user.profile.save()
            return redirect('/superviseurs/list')
        else:
            print(form.errors())
            return render(request, 'update-admin.html', locals())
    else:
        form = UpdateAdminForm()
        return render(request, 'update-admin.html', locals())

@login_required
def superviseur_details(request: HttpRequest, *args, **kwargs):
    contexte = dict()
    contexte['superviseur'] = request.user
    contexte['profile'] = Profile.objects.get(user=request.user)
    return render(request, 'admin.html', contexte)

@login_required
def delete_admin(request: HttpRequest, *args, **kwargs):
    """ Vue e suppression d'un administrateur """
    if request.method == "POST":
        request.user.delete()
        return redirect('/login')
    else:
        return render(request, 'whats-up.html', {})

class SuperviseurList(LocalLoginRequired, ListView):
    model = User
    template_name = "admins.html"
    context_object_name = 'superviseurs'



