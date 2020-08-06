from django.shortcuts import render, redirect
from django.views.generic import View
from django.core import serializers
from django.http import HttpResponse, Http404

from .models import ReglagesGeneral

from app.views import LocalLoginRequired
from compteur.models import Classe

class ReglagesUpdateView(LocalLoginRequired, View):
    def get(self, request, *args, **kwargs):
        classe1 = Classe.objects.get(id=1)
        classe2 = Classe.objects.get(id=2)
        classe3 = Classe.objects.get(id=3)

        settings = ReglagesGeneral.objects.get(id=1)

        return render(request, "reglages.html", locals())

class ClassesUpdateView(LocalLoginRequired, View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            try:
                datas = request.POST
                classe1 = Classe.objects.get(id=1)
                classe1.p_max = float(datas["p_max_dom"])
                classe1.q_max = float(datas["q_max_dom"])
                classe1.save()

                classe2 = Classe.objects.get(id=2)
                classe2.p_max = float(datas["p_max_semi_ind"])
                classe2.q_max = float(datas["q_max_semi_ind"])
                classe2.save()

                classe3 = Classe.objects.get(id=3)
                classe3.p_max = float(datas["p_max_ind"])
                classe3.q_max = float(datas["q_max_ind"])
                classe3.save()

                return HttpResponse("ok")
            
            except:
                return HttpResponse("error")
        
        else:
            return Http404("Page indisponible")
    
class GeneralSettingsUpdateView(LocalLoginRequired, View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            try:
                datas = request.POST
                settings = ReglagesGeneral.objects.get(id=1)
                settings.prix_par_watt = datas["prix_par_watt"]
                settings.min_alert_compteurs = datas["min_alert_compteurs"]
                settings.min_alert_transfos = datas["min_alert_transfos"]

                settings.save()
                
                return HttpResponse("ok")
            except:
                return HttpResponse("error") 
        else:
            return Http404("Page indisponible")