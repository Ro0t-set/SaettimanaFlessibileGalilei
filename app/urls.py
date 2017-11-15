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
    url(r'^help/$', views.help, name='help'),
    url(r'^tabelle/$', views.tabelle, name='tabelle'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^filtro_fasce/$', views.filtro_fasce, name='filtro_fasce'),
    url(r'^errore/$', views.errore, name='errore'),
    url(r'^successo/$', views.successo, name='successo'),
    url(r'^(?P<corso_id>[0-9]+)/edit/$', views.edit_iscrizioni, name='edit_iscrizioni'),



]
