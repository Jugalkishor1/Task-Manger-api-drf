#!/bin/sh

echo "📡 Waiting for PostgreSQL to be ready..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.5
done

echo "✅ PostgreSQL is up!"

echo "🔁 Running migrations..."
python manage.py migrate

echo "🚀 Starting Django server..."
python manage.py runserver 0.0.0.0:8000
