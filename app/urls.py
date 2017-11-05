from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from app.models import Corso
from django.contrib.auth.views import login, logout



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^crea/$', views.crea, name='crea'),
#    url(r'^iscrizioni/$', views.iscrizioni, name='iscrizioni'),
    url(r'^privata/$', views.privata, name='privata'),
    url(r'^filtro_fasce/$', views.filtro_fasce, name='filtro_fasce'),
    url(r'^edit/$', views.edit_iscrizioni, name='edit_iscrizioni'),



]
