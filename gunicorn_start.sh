#!/bin/bash

NAME="appointments"                              #Name of the application (*)
DJANGODIR=/home/king/Documentos/proyectos/backend-appointments/appointments          # Django project directory (*)
SOCKFILE=/home/king/Documentos/proyectos/backend-appointments/appointments/run/gunicorn.sock        # we will communicate using this unix socket (*)
USER=nginx                                        # the user to run as (*)
GROUP=webdata                                     # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=appointments.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=appointments.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
pwd
#source /home/king/Documentos/proyectos/envs/appointments/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/king/Documentos/proyectos/envs/appointments/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --bind=unix:$SOCKFILE