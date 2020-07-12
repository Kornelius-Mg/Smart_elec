from django.shortcuts import render, redirect

def reglages(request, *args, **kwargs):
    return render(request, "reglages.html", locals())