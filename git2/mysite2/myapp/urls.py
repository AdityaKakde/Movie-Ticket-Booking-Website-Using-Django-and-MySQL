#from django.contrib import admin
from django.conf.urls import re_path
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    re_path(r'^$', views.index),
    re_path(r'index/$', views.index),
    re_path(r'adminLobby/$', views.adminLobby),
    re_path(r'adminLogin/$', views.adminLogin),
    re_path(r'createEvent/$', views.createEvent),
    re_path(r'createAccount/$', views.createAccount),
    re_path(r'login/$', views.login),
]
