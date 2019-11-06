#!/bin/sh

echo "Iniciando PostgreSQL..."

while ! timeout 1 bash -c "echo > /dev/tcp/postgresql/5432"; do   
  sleep 1
done

echo "PostgreSQL iniciado."

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
