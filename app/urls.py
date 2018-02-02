from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from app.models import Corso
from django.contrib.auth.views import login, logout



urlpatterns = [
    url(r'^$', views.home, name='home'),
#    url(r'^crea/$', views.crea, name='crea'),
#    url(r'^iscrizioni/$', views.iscrizioni, name='iscrizioni'),
    url(r'^privata/$', views.privata, name='privata'),
    url(r'^help/$', views.help, name='help'),
    url(r'^tabelle/$', views.tabelle, name='tabelle'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^filtro_fasce/$', views.filtro_fasce, name='filtro_fasce'),
    url(r'^errore/$', views.errore, name='errore'),
    url(r'^successo/$', views.successo, name='successo'),
    url(r'^errorefasciapiena/$', views.errorefasciapiena, name='errorefasciapiena'),
    url(r'^(?P<corso_id>[0-9]+)/elimina/$', views.elimina, name='elimina'),
    url(r'^(?P<corso_id>[0-9]+)/edit/$', views.edit_iscrizioni, name='edit_iscrizioni'),
    url(r'^(?P<corso_id>[0-9]+)/appello/$', views.appelli, name='appelli'),
    url(r'^disp_classi_palestra/$', views.disp_classi_palestra,  name='disp_classi_palestra'),
    url(r'^disp_classi_magna/$', views.disp_classi_magna,  name='disp_classi_magna'),
    url(r'^disp_classi_informatica/$', views.disp_classi_informatica,  name='disp_classi_informatica'),
    url(r'^disp_classi_arte/$', views.disp_classi_arte,  name='disp_classi_arte'),
    url(r'^disp_classi/$', views.disp_classi,  name='disp_classi'),
]
