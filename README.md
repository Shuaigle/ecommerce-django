# Ecommerce-Django

Ecommerce-Django is a website built mainly in django and django rest framework.

## Features

-  test-driven development with factory_boy and pytest
-  Django 4.0
-  PostgreSQL docker image
-  docker-compose
-  elasticsearch

## Usage

``git clone https://github.com/Shuaigle/ecommerce-django.git``
install requirements packages
``pip install -r requirements.txt``
then delete the migration files in ecommerce/inventory/migrations/000*.py.
load data into database
``python3 manage.py load-fixtures``