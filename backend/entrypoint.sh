#!/bin/sh

echo "Waiting for PostgreSQL to be ready..."
while ! nc -z postgresdb 5432; do
  sleep 1
done

echo "PostgreSQL started"

python manage.py migrate
#!/bin/sh

echo "Waiting for PostgreSQL to be ready..."
while ! nc -z postgresdb 5432; do
  sleep 1
done

echo "PostgreSQL started"

python manage.py migrate
python manage.py runserver 0.0.0.0:8000

