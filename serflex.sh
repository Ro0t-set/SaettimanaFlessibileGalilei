#!/bin/sh
### BEGIN INIT INFO
# Provides: setflex
# Required-Start:
# Required-Stop:
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Avvio automatico del sito
# Description: Servizio per ovviare il precedente malfuzionante
### END INIT INFO

DESC="setflex"
NAME=setflex
alias proj="cd /home/django/django_project"

do_start()
{
   echo "starting!";
   cd /home/django/django_project;
   echo "Trovata Cartella!!";
   exec gunicorn --workers 3 -b 0.0.0.0:80 django_project.wsgi;
   echo "Avvio eseguito con successo!";
}


do_stop()
{
   echo "stopping!"
}


case "$1" in
   start)
     do_start
     ;;
   stop)
     do_stop
     ;;
esac