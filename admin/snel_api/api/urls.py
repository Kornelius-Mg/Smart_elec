from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (UtilisateurViewsSet, AppartementViewsSet, CompteurViewsSet, 
                    TransfertViewsSet, TransformateurViewsSet, AchatViewsSet)


router =routers.DefaultRouter()
router.register(r'users',UtilisateurViewsSet)
router.register(r'appartement',AppartementViewsSet)
router.register(r'compteur',CompteurViewsSet)
router.register(r'transfert', TransfertViewsSet)
router.register(r'achat', AchatViewsSet),
router.register(r'transfo', TransformateurViewsSet)

urlpatterns = [
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
