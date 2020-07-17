from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    	path('list/', AchatsList.as_view(), name='achats'),
		path('new/', AchatCreateView.as_view(), name="new-achat"),
		url(r'^update/(?P<pk>[0-9]+)/$', AchatUpdateView.as_view(), name="update-achat"),
		url(r'^delete/(?P<pk>[0-9]+)/$', AchatDeleteView.as_view(), name="delete-achat"),
]