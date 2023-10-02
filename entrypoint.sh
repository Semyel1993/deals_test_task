#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py createsuperuser --username 'admin' --email 'admin@mail.com' --no-input
python manage.py runserver 0.0.0.0:8000