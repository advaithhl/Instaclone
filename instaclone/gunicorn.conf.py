import multiprocessing
from os import getenv as os_getenv


bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
wsgi_app = 'instaclone.wsgi:application'

loglevel = 'info'

if os_getenv('INSTACLONE_DJANGO_DEBUG_MODE') == 'debug':
    loglevel = 'debug'
    reload = True
