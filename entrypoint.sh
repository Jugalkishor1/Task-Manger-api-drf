#!/bin/sh

echo "📡 Waiting for PostgreSQL to be ready..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.5
done

echo "PostgreSQL is up!"

echo "Running migrations..."
python manage.py migrate

echo "Create Super User....."
python manage.py createadmin

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000
