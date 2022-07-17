#!/bin/sh

# Execute celery as the PID 1 process.
exec celery -A instaclone worker -l INFO
