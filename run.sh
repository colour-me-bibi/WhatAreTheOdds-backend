#!/usr/bin/env bash

wait-for-it postgres:5432 --strict -- echo "Postgres is up"

python manage.py makemigrations
python manage.py migrate
# python manage.py loaddata fixtures/initial_data.json
python manage.py collectstatic --noinput

uvicorn backend.asgi:application --reload --host 0.0.0.0 --port 8000
