from django.shortcuts import render, redirect
from django.views.generic import View
from app.views import LocalLoginRequired

class ReglagesUpdateView(LocalLoginRequired, View):
    def get(self, request, *args, **kwargs):
        return render(request, "reglages.html", locals())
    
    def post(self, request, *args, **kwargs):
        return render(request, "reglages.html")


