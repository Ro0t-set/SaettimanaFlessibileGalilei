# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


# Create your models here.
class Aula(models.Model):
    aule= models.CharField(max_length=100, default="")
    max_iscritti= models.IntegerField(default=0)
    def __str__(self):
        return str(self.aule)




class Corso(models.Model):
    titolo = models.CharField(max_length=100)
    studenti_referenti= models.CharField(max_length=100)
    descrizione= models.TextField(blank=True)
    classi_autori = models.CharField(max_length=10, default="")
    aule = models.ForeignKey('Aula')


    progressivo= models.BooleanField(default=False)

    f1= models.BooleanField(default=False)
    f2= models.BooleanField(default=False)
    f3= models.BooleanField(default=False)
    f4= models.BooleanField(default=False)
    f5= models.BooleanField(default=False)
    f6= models.BooleanField(default=False)
    f7= models.BooleanField(default=False)
    f8= models.BooleanField(default=False)







    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.titolo)




class Iscrizione(models.Model):

    user = models.ForeignKey('auth.User')
    corso1= models.ForeignKey('Corso', blank=True, null=True, related_name="corso1")
    corso2= models.ForeignKey('Corso', blank=True, null=True, related_name="corso2")
    corso3= models.ForeignKey('Corso', blank=True, null=True, related_name="corso3")
    corso4= models.ForeignKey('Corso', blank=True, null=True, related_name="corso4")
    corso5= models.ForeignKey('Corso', blank=True, null=True, related_name="corso5")
    corso6= models.ForeignKey('Corso', blank=True, null=True, related_name="corso6")
    corso7= models.ForeignKey('Corso', blank=True, null=True, related_name="corso7")
    corso8= models.ForeignKey('Corso', blank=True, null=True, related_name="corso8")






    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return str(self.user)
