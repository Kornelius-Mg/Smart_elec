from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, Http404
from superviseur.models import Profile
from .forms import *

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

def register_form(request: HttpRequest, *args, **kwargs):
    print(request.method)
    if request.method == "POST":
        form = RegisterAdminForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            user = User.objects.create_user(username, email, password)
            user.firstname = form.cleaned_data["firstname"]
            user.lastname = form.cleaned_data["lastname"]
            profile = Profile(user=user)
            profile.telephone = form.cleaned_data["telephone"]
            if form.cleaned_data["avatar"]:
                profile.avatar = form.cleaned_data["avatar"]
            profile.save()
            user = authenticate(username=username, password=password)
            if user:
                return redirect('')
            else:
                return render(request, 'create-admin.html', {'error': 'Une erreur s\'est produite, veuillez recommencer s\'il vous plait'})
        else:
            return render(request, 'create-admin.html', {})
    else:
        form = RegisterAdminForm()
        return render(request, 'create-admin.html', {})
