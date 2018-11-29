#from django.contrib import admin
from django.conf.urls import re_path
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    re_path(r'^$', views.index),
    re_path(r'index/$', views.index),
    re_path(r'adminLobby/$', views.adminLobby),
    re_path(r'managerRegister/$', views.managerRegister_view),
    re_path(r'managerLogin/$', views.managerLogin_view),
    re_path(r'createEvent/$', views.create_event_view),
    re_path(r'eventScreen$', views.eventScreen,name='eventScreen'),
    re_path(r'createAccount/$', views.createAccount),
    #re_path(r'login/$', views.login),
    re_path(r'managerLogin/$', views.managerLogin),
    re_path(r'signup/$', views.signup_view),
    re_path(r'login/$', views.login_view),
    re_path(r'logout/$', views.logout_view)
    # re_path(r'signupform/$', views.signupform),
    #re_path(r'managerLogin|/createAccount|/createEvent|/adminLogin|/createEvent/index/$', views.index),
]
