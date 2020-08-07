"""snel_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from app.views import *
import api
import superviseur, user, compteur, parametres, transfos, achats, transferts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')), 
    path('compteurs/', include('compteur.urls')),
    path('transfos/', include('transfos.urls')),
    path('reglages/', include('parametres.urls')),
    path('achats/', include('achats.urls')),
    path('transferts/', include('transferts.urls')),
    path('api/', include('api.urls')),
    path('', include('app.urls')),
    path('', include('superviseur.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)