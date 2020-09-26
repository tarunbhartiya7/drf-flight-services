python3 -m venv env
source env/bin/activate
pip install django
pip install djangorestframework
django-admin startproject flightServices .
django-admin startapp flightApp
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
