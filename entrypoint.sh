#!/bin/sh

echo "⏳ Waiting for PostgreSQL to be ready..."

until python -c "import socket; socket.create_connection(('${DB_HOST}', int('${DB_PORT}')))" 2>/dev/null; do
  echo "Still waiting for PostgreSQL..."
  sleep 1
done

echo "✅ PostgreSQL is up!"

echo "🔁 Running migrations..."
python manage.py migrate

echo "👤 Creating superuser (if not exists)..."
python manage.py createadmin

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "🚀 Starting Django server..."
python manage.py runserver 0.0.0.0:8000
