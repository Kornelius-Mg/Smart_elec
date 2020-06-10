from django.urls import path, include
from AdminApp.views import HomeView, UserCreateView, UserDeleteView, UserListView, UserUpdateView, UserDetailView
from django.conf.urls import url


urlpatterns = [
     path('', HomeView.as_view(), name="home"),
     path('users/new', UserCreateView.as_view(), name="new-user"),
     path('users/', UserListView.as_view(), name="users"),
     url(r'^users/delete/(?P<pk>[0-9]+)/$', UserDeleteView.as_view(), name="delete-user"),
     url(r'^users/update/(?P<pk>[0-9]+)/$', UserUpdateView.as_view(), name="update-user"),
     url(r'^user/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name="user")
]