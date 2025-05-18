#!/bin/sh

set -e

echo "📡 Waiting for PostgreSQL at $DB_HOST:$DB_PORT..."

# Wait for PostgreSQL to be ready
until nc -z $DB_HOST $DB_PORT; do
  echo "⏳ Waiting for database..."
  sleep 1
done

echo "✅ PostgreSQL is up!"

echo "🔧 Running migrations..."
python manage.py migrate --noinput

echo "👤 Creating admin user..."
python manage.py createadmin || true

echo "🎯 Collecting static files..."
python manage.py collectstatic --noinput

echo "🚀 Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000
