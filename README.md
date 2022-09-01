# LAB-33 Django auth
Base on previous lab, add auth functionality by using JWT

## project: 
drf-api-auth-postgres
## Author: 
Rui Guo
## setup

- alias venv.
- pip install django
- pip freeze > requirements.txt
- django-admin startproject
- python manage.py migrate
- python manage.py runserver
- python manage.py startapp
- python manage.py makemigrations
- python manage.py migrate
- python manage.py creatsuperuser
- python manage.py runserver
## Docker
- docker compose build
- docker compose up
- docker compose up --build

## test

python manage.py test


