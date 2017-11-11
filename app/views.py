# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Corso, Iscrizione
from django.shortcuts import get_object_or_404, render
from .forms import CreaCorsi, IscrizioneForm, Mail
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
import operator
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
import datetime
from django.db.models import Q
from django.forms import formset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Count
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator

@csrf_protect


def crea(request):
#    corsi= Corso.objects.all()
#    print (corsi.count())
#    print ('funge')
#    if corsi.count() > 4:
#        print('errore')
#    else:
#        print('successo')





    if request.method == "POST":

        form = CreaCorsi(request.POST)

        if form.is_valid():

            corso = form.save(commit=False)
            corso.author = request.user
            corso.published_date = timezone.now()
            corso.save()
            subject, from_email, to = 'corsi', 'settimanaflessibile@gmail.com', 'settimanaflessibile@gmail.com'
            text_content = '456'
            html_content =  form.cleaned_data['titolo']

            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            # corsixl = Workbook()
            # dest_filename = 'tabelle/corsi.xlsx'
            # wcorsi= corsixl.active
            # wcorsi = corsixl.create_sheet(title="corsi")
            # colonnaA="A"
            # rigaecolonna= colonnaA[(corso.id+1)]
            # print rigaecolonna
            #
            # wcorsi['A1'] = "titolo"
            # wcorsi['B1'] = "descrizione"
            # wcorsi['C1'] = "autori"
            # wcorsi['D1'] = "classe autori"
            # wcorsi[rigaecolonna] = corso.titolo


            #corsixl.save(filename = 'tabelle/corsi.xlsx')
            return redirect('home')

    else:
        form = CreaCorsi()

    return render(request, 'corsi/crea.html', {'form' : form })

@login_required(login_url='/login/')
def home (request):
     corsi = Corso.objects.all()

     return render(request, 'corsi/home.html', {'corsi': corsi})

def tabelle (request):
     corsi = Corso.objects.all()


     return render(request, 'corsi/tabelle.html', {'corsi': corsi})



@login_required(login_url='/login/')
def privata(request):

    iscrizioni= Iscrizione.objects.filter(user=request.user)


    return render(request, 'corsi/privata.html', {'iscrizioni':iscrizioni})


@login_required(login_url='/login/')
def edit_iscrizioni(request, corso_id):
    corsi = Corso.objects.filter( pk=corso_id)
    fasca = Corso.objects.get( pk=corso_id)
    tabella= Iscrizione.objects.filter(user=request.user)
    iscrizione=get_object_or_404(Iscrizione, pk=tabella)

    if request.method == "POST":
        form = IscrizioneForm(request.POST, instance= iscrizione)
        if form.is_valid():
            iscrizione = form.save(commit=False)
            iscrizione.user = request.user
            iscrizione.published_date = timezone.now()
            if fasca.progressivo:

                if fasca.f1:
                    iscrizione.corso1 = fasca
                if fasca.f2:
                    iscrizione.corso2 = fasca

                if fasca.f3:
                    iscrizione.corso3_id= fasca
                if fasca.f4:
                    iscrizione.corso4_id= fasca
                if fasca.f5:
                    iscrizione.corso5_id= fasca
                if fasca.f6:
                    iscrizione.corso6_id= fasca
                if fasca.f7:
                    iscrizione.corso7_id= fasca
                if fasca.f8:
                    iscrizione.corso8_id= fasca
                if fasca.f9:
                    iscrizione.corso9_id= fasca
            iscrizione.save()


        return redirect('privata')

    else:
        form = IscrizioneForm(instance= iscrizione)
    return render(request, 'corsi/edit.html', {'form':form, 'corsi':corsi})


# @login_required
# def iscrizioni(request, id):
#
#
#     corsi = request.GET.get("a")
#     if corsi:
#         corsi = Corso.objects.filter(id= corsi)
#         corsi = get_object_or_404(iscrizioni, id=id)
#
#
#
#         if request.method == 'POST':
#             form = IscrizioneForm(request.POST, corsi=corsi )
#             if form.is_valid():
#                 iscrizione = form.save(commit=False)
#                 iscrizione.user = request.user
#                 iscrizione.published_date = timezone.now()
#                 iscrizione.save()
#                 return redirect('home')
#
#
#         else:
#             form = IscrizioneForm()
#     return render(request, 'corsi/iscrizioni.html', {'corsi' : corsi, 'form':form })

@login_required(login_url='/login/')
def filtro_fasce(request):
    corsi=request.GET.get("f")
    if corsi == 'f1':
        corsi = Corso.objects.filter(f1=True)
    if corsi == 'f2':
        corsi = Corso.objects.filter(f2=True)
    if corsi == 'f3':
        corsi = Corso.objects.filter(f3=True)
    if corsi == 'f4':
        corsi = Corso.objects.filter(f4=True)
    if corsi == 'f5':
        corsi = Corso.objects.filter(f5=True)
    if corsi == 'f6':
        corsi = Corso.objects.filter(f6=True)
    if corsi == 'f7':
        corsi = Corso.objects.filter(f7=True)
    if corsi == 'f8':
        corsi = Corso.objects.filter(f8=True)
    if corsi == 'f9':
        corsi = Corso.objects.filter(f9=True)
    return render(request, 'corsi/filtro_fasce.html', {'corsi' : corsi})

def help(request):
    if request.method == "POST":
        form = Mail(request.POST)
        if form.is_valid():
            subject, from_email, to = 'problemi', 'settimanaflessibile@gmail.com', 'settimanaflessibile@gmail.com'
            text_content = '456'
            html_content =  form.cleaned_data['testo']
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
    else:
        form = Mail()
    return render(request, 'corsi/help.html', {'form': form})
