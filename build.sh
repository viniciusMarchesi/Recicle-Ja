#!/usr/bin/env bash
# Script de build para o Render
set -o errexit

# Instala dependências
pip install -r requirements.txt

# Coleta arquivos estáticos
python manage.py collectstatic --noinput

# Aplica migrações no banco de dados
python manage.py migrate

# Popula o banco de dados com dados iniciais
python manage.py shell < populate_db.py
