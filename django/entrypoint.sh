#!/bin/sh

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --no-input
#cp -r bkp/media/ .

exec "$@"