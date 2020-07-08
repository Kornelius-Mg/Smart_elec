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
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app.views import *
import superviseur, user, compteur, parametres, transfos

router =routers.DefaultRouter()
router.register(r'users',UtilisateurViewsSet)
router.register(r'appartement',AppartementViewsSet)
router.register(r'compteur',CompteurViewsSet)
router.register(r'details-compteur', DetailsCompteurViewsSet)
router.register(r'Abonnement', AbonnementViewsSet)
router.register(r'transfert', TransfertViewsSet)
router.register(r'adresse', AdresseViewsSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('users/', include('user.urls')), 
    path('compteurs/', include('compteur.urls')),
    path('transfos/', include('transfos.urls')),
    path('', include('app.urls')),
    path('', include('superviseur.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)