# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Corso,  Iscrizione, Aula


# Register your models here.

admin.site.register(Corso)
admin.site.register(Aula)
admin.site.register(Iscrizione)
