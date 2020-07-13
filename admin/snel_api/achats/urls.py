from django.urls import path
from .views import *

urlpatterns = [
    	path('list/', AchatsList.as_view(), name='achats'),
		path('new/', AchatCreateView.as_view(), name="new-achat"),
]