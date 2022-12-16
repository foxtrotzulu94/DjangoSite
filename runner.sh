#!/bin/bash
echo Making Migrations...
python manage.py makemigrations --noinput

echo Migrating...
python manage.py migrate --noinput

if [[ -z $DEBUG || $DEBUG -eq 0 ]];
then
    echo Running production server on port 8000
    gunicorn --bind localhost:8000 domain.wsgi:application
else
    echo Running debug server on port 7654
    python manage.py runserver 0.0.0.0:7654
fi
