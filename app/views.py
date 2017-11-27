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


    if request.method == "POST":

        form = CreaCorsi(request.POST)

        if form.is_valid():

            corso = form.save(commit=False)
            corso.author = request.user
            corso.published_date = timezone.now()



            subject, from_email, to = 'corsi', 'settimanaflessibile@gmail.com', 'settimanaflessibile@gmail.com'
            text_content = '456'
            html_content =  (
            '<style>table{border-collapse:collapse}td, th { border:1px solid #ddd;padding:8px;}</style>' +
            '<table><tr><td>Titolo</td><td>Studenti Referenti</td><td>Classi Studenti Referenti</td><td>Descrizione del Corso</td></tr>' +
            '<tr><td>' + form.cleaned_data['titolo'] + '</td><td>' + form.cleaned_data['studenti_referenti'] + '</td></tr> </table>')





            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            corso.save()

            return redirect('successo')

    else:
        form = CreaCorsi()

    return render(request, 'corsi/crea.html', {'form' : form })


def home (request):
     corsi = Corso.objects.all()

     return render(request, 'corsi/home.html', {'corsi': corsi})

def tabelle (request):
     corsi = Corso.objects.all()
     appelli = Iscrizione.objects.filter(corso1=corsi)
     print (appelli)

     return render(request, 'corsi/tabelle.html', {'corsi': corsi, 'appelli':appelli})



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
    classe_max= fasca.aule.max_iscritti
    singoli=request.GET.get("f")


    contatore1= Iscrizione.objects.filter(corso1_id=fasca)
    contatore2= Iscrizione.objects.filter(corso2_id=fasca)
    contatore3= Iscrizione.objects.filter(corso3_id=fasca)
    contatore4= Iscrizione.objects.filter(corso4_id=fasca)
    contatore5= Iscrizione.objects.filter(corso5_id=fasca)
    contatore6= Iscrizione.objects.filter(corso6_id=fasca)
    contatore7= Iscrizione.objects.filter(corso7_id=fasca)
    contatore8= Iscrizione.objects.filter(corso8_id=fasca)

    if singoli=='f1':
        contatore=contatore1.count()
    if singoli=='f2':
        contatore=contatore2.count()
    if singoli=='f3':
        contatore=contatore3.count()
    if singoli=='f4':
        contatore=contatore4.count()
    if singoli=='f5':
        contatore=contatore5.count()
    if singoli=='f6':
        contatore=contatore6.count()
    if singoli=='f7':
        contatore=contatore7.count()
    if singoli=='f8':
        contatore=contatore8.count()


    print (contatore)


    print("numero massimo:",classe_max)

    if contatore>=classe_max:
        return redirect('errore')
    else:


        if request.method == "POST":
            form = IscrizioneForm(request.POST, instance= iscrizione)


            if form.is_valid():
                iscrizione = form.save(commit=False)
                iscrizione.user = request.user
                iscrizione.published_date = timezone.now()
                if fasca.progressivo:
                    if contatore<classe_max:
                        if fasca.f1:
                            iscrizione.corso1 = fasca
                        if fasca.f2:
                            iscrizione.corso2 = fasca
                        if fasca.f3:
                            iscrizione.corso3= fasca
                        if fasca.f4:
                            iscrizione.corso4= fasca
                        if fasca.f5:
                            iscrizione.corso5= fasca
                        if fasca.f6:
                            iscrizione.corso6= fasca
                        if fasca.f7:
                            iscrizione.corso7= fasca
                        if fasca.f8:
                            iscrizione.corso8= fasca
                    else:
                        return redirect('errore')


                else:
                    if contatore<classe_max:
                        if fasca.f1 and singoli=='f1':
                            iscrizione.corso1_id = fasca
                        elif fasca.f2 and singoli=='f2':
                            iscrizione.corso2_id = fasca
                        elif fasca.f3 and singoli=='f3':
                            iscrizione.corso3_id= fasca
                        elif fasca.f4 and singoli=='f4':
                            iscrizione.corso4_id= fasca
                        elif fasca.f5 and singoli=='f5':
                            iscrizione.corso5_id= fasca
                        elif fasca.f6 and singoli=='f6':
                            iscrizione.corso6_id= fasca
                        elif fasca.f7 and singoli=='f7':
                            iscrizione.corso7_id= fasca
                        elif fasca.f8 and singoli=='f8':
                            iscrizione.corso8_id= fasca
                    else:
                        return redirect('errore')


            iscrizione.save()
            return redirect('successo')

        else:
            form = IscrizioneForm(instance= iscrizione)

        return render(request, 'corsi/edit.html', {'form':form, 'corsi':corsi, 'contatore':contatore})



@login_required(login_url='/login/')
def filtro_fasce(request):

    corsi=request.GET.get("f")


    if corsi == 'f1':
        corsi = Corso.objects.filter(f1=True)
        fascia= 'f1'
    if corsi == 'f2':
        corsi = Corso.objects.filter(f2=True)
        fascia= 'f2'
    if corsi == 'f3':
        corsi = Corso.objects.filter(f3=True)
        fascia= 'f3'
    if corsi == 'f4':
        corsi = Corso.objects.filter(f4=True)
        fascia= 'f4'
    if corsi == 'f5':
        corsi = Corso.objects.filter(f5=True)
        fascia= 'f5'
    if corsi == 'f6':
        corsi = Corso.objects.filter(f6=True)
        fascia= 'f6'
    if corsi == 'f7':
        corsi = Corso.objects.filter(f7=True)
        fascia= 'f7'
    if corsi == 'f8':
        corsi = Corso.objects.filter(f8=True)
        fascia= 'f8'



    return render(request, 'corsi/filtro_fasce.html', {'corsi' : corsi, 'fascia': fascia})

@login_required(login_url='/login/')
def elimina(request, corso_id):

    corsi = Corso.objects.filter( pk=corso_id)
    fasca = Corso.objects.get( pk=corso_id)
    tabella= Iscrizione.objects.filter(user=request.user)
    iscrizione=get_object_or_404(Iscrizione, pk=tabella)
    classe_max= fasca.aule.max_iscritti
    singoli=request.GET.get("f")

    if request.method == "POST":
        form = IscrizioneForm(request.POST, instance= iscrizione)


        if form.is_valid():
            iscrizione = form.save(commit=False)
            iscrizione.user = request.user
            iscrizione.published_date = timezone.now()
            if fasca.progressivo:

                if fasca.f1:
                    iscrizione.corso1_id = ''
                if fasca.f2:
                    iscrizione.corso2_id = ''
                if fasca.f3:
                    iscrizione.corso3_id= ''
                if fasca.f4:
                    iscrizione.corso4_id= ''
                if fasca.f5:
                    iscrizione.corso5_id= ''
                if fasca.f6:
                    iscrizione.corso6_id= ''
                if fasca.f7:
                    iscrizione.corso7_id= ''
                if fasca.f8:
                    iscrizione.corso8_id= ''
            else:

                if fasca.f1 and singoli=='f1':
                    iscrizione.corso1_id = ''
                elif fasca.f2 and singoli=='f2':
                    iscrizione.corso2_id = ''
                elif fasca.f3 and singoli=='f3':
                    iscrizione.corso3_id= ''
                elif fasca.f4 and singoli=='f4':
                    iscrizione.corso4_id= ''
                elif fasca.f5 and singoli=='f5':
                    iscrizione.corso5_id= ''
                elif fasca.f6 and singoli=='f6':
                    iscrizione.corso6_id= ''
                elif fasca.f7 and singoli=='f7':
                    iscrizione.corso7_id= ''
                elif fasca.f8 and singoli=='f8':
                    iscrizione.corso8_id= ''
                else:
                    return redirect('privata')


        iscrizione.save()
        return redirect('privata')

    else:
        form = IscrizioneForm(instance= iscrizione)

    return render(request, 'corsi/elimina.html', {'form':form, 'corsi':corsi})


def help(request):
    if request.method == "POST":
        form = Mail(request.POST)
        if form.is_valid():
            subject, from_email, to = form.cleaned_data['mail'], 'settimanaflessibile@gmail.com', 'settimanaflessibile@gmail.com'
            text_content = '456'
            html_content =  form.cleaned_data['testo']
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send(fail_silently=False)
            return redirect('successo')
    else:
        form = Mail()
    return render(request, 'corsi/help.html', {'form': form})



def errore(request):
    return render(request, 'corsi/errore.html')

def successo(request):
    return render(request, 'corsi/successo.html')
