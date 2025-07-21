#!/bin/sh

set -e

cd /app_root

# .env を読み込む
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

echo "Waiting for DB to be ready..."
until pg_isready -h "${DATABASE_SERVER}" -p "${DATABASE_PORT}" -U "${DATABASE_USER}"; do
  echo "PostgreSQL is not ready yet. Waiting..."
  sleep 1
done

echo "Running Alembic migrations..."
alembic upgrade head
