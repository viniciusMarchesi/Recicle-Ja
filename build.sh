#!/usr/bin/env bash
# Script de build para o Render
set -o errexit

# Instala dependências
pip install -r requirements.txt

# Coleta arquivos estáticos
python manage.py collectstatic --noinput

# Aplica migrações no banco de dados
python manage.py migrate

# Cria superusuário automaticamente se as variáveis estiverem definidas
if [[ -n "${DJANGO_SUPERUSER_USERNAME}" && -n "${DJANGO_SUPERUSER_PASSWORD}" && -n "${DJANGO_SUPERUSER_EMAIL}" ]]; then
  echo "Criando superusuário..."
  python manage.py createsuperuser --noinput || echo "Superusuário já existe ou ocorreu um erro."
fi
