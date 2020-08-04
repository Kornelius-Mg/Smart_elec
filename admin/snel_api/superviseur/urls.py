from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SuperviseurList, superviseur_details, superviseur_update, delete_admin, register_form

urlpatterns = [
    # URLS d'authentification

    url(r'^logout/$', LogoutView.as_view(template_name="login.html"), name="logout"),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name="login"),
    url(r'^register/$', register_form, name="register"),

    path('superviseurs/list/', SuperviseurList.as_view(), name='list-superviseurs'),
    url(r'^superviseurs/details/(?P<pk>[a-zA-Z0-9]+)/$', superviseur_details, name='superviseur'),
    
    url(r'^superviseur/delete/(?P<pk>[a-zA-Z0-9]+)/$',  delete_admin, name='delete-admin'),
    url(r'^superviseur/update/(?P<pk>[a-zA-Z0-9]+)/$', superviseur_update, name='update-admin'),
]