#!/bin/sh

# Perform DB migration.
python manage.py migrate --no-input

# Collect static files to STATIC_ROOT of django.
python manage.py collectstatic --no-input

# Execute gunicorn as the PID 1 process.
exec gunicorn
