from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index),
    path('adminLobby/', views.adminLobby),
    path('adminLogin/', views.adminLogin),
    path('createEvent/', views.createEvent),
    path('createAccount/', views.createAccount),
]
