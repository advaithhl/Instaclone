#!/bin/sh

# Remove Python requirements.txt.
rm requirements.txt

# Remove Docker entrypoint scripts.
rm *docker-entrypoint.sh

# Remove gunicorn config file.
rm gunicorn.conf.py

# Execute celery as the PID 1 process.
exec celery -A instaclone worker -l INFO
