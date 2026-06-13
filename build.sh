#!/usr/bin/env bash
# Script de build para o Render
set -o errexit

# Instala dependências
pip install -r requirements.txt

# Coleta arquivos estáticos
python manage.py collectstatic --noinput

# Aplica migrações no banco de dados
python manage.py migrate

# Inicializa o banco de dados e cria superusuário de forma segura
python init_db_prod.py
