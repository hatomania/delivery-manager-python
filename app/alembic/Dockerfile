ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

WORKDIR /project_root

COPY . .

RUN \
pip install --upgrade pip && \
pip install --no-cache-dir -r ./app/alembic/requirements.txt && \
chmod +x ./app/alembic/run_migration.sh && \
apt update && apt -y install postgresql-client && \
find /var/lib/apt/lists/ -mindepth 1 -maxdepth 1 -type d,f | xargs rm -rf

ENTRYPOINT ["sh", "./app/alembic/run_migration.sh"]
