#!/bin/sh


python manage.py makemigrations --noinput
python manage.py migrate --noinput
DJANGO_SUPERUSER_PASSWORD="$DJANGO_SUPERUSER_PASSWORD" python manage.py createsuperuser --username "$DJANGO_SUPERUSER_USERNAME" --email "$DJANGO_SUPERUSER_EMAIL" --noinput
python manage.py runserver 0.0.0.0:8000