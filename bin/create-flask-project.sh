#!/bin/bash

mkdir $1
mkdir -p $1/app
touch $1/app/__init__.py $1/app/models.py 
mkdir -p $1/app/templates
mkdir -p $1/app/static
mkdir -p $1/app/main
touch $1/app/main/__init__.py $1/app/main/errors.py $1/app/main/forms.py $1/app/main/views.py
mkdir -p $1/migrations
mkdir -p $1/tests
touch $1/tests/__init__.py $1/tests/test.py
touch $1/requeriments.txt $1/config.py $1/manage.py

echo "flask==0.11" >> $1/requeriments.txt

virtualenv $1/venv
cd $1
source venv/bin/activate
pip install -r requeriments.txt
