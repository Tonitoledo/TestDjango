#!/bin/bash

echo "➡️ Instalando dependencias..."
sudo apt update
sudo apt install python3 python3-venv python3-pip mysql-server libmysqlclient-dev -y

echo "➡️ Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

echo "➡️ Instalando requirements..."
pip install -r requirements.txt

echo "✅ Entorno instalado. Asegúrate de haber creado la base de datos en MySQL:"
echo
echo "    CREATE DATABASE simpleERP CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
echo "    CREATE USER 'toni'@'localhost' IDENTIFIED BY '1234';"
echo "    GRANT ALL PRIVILEGES ON simpleERP.* TO 'toni'@'localhost';"
echo "    FLUSH PRIVILEGES;"
echo
echo "📦 Luego ejecuta:"
echo "    source venv/bin/activate"
echo "    python manage.py migrate"
echo "    python manage.py runserver"