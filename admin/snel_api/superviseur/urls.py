from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    # URLS d'authentification

     url(r'^login-admin/$', login_admin, name="login-admin"),
     url(r'^logout/$', LogoutView.as_view(template_name="login.html"), name="logout"),
     url(r'^login/$', LoginView.as_view(template_name='login.html'), name="login"),
     url(r'^register/$', register_form, name="register"),
]