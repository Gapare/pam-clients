#!/bin/bash

# Install requirements
pip install -r requirements.txt

# Make sure static directory exists
mkdir -p static

# Collect static files
python manage.py collectstatic --noinput
