@echo off
echo [DEV-Server] Starting...
echo [DEV-Server] __load__
cd UI
echo [DEV-Server] Starting web...
start http://localhost:8000
echo [DEV-Server] Waiting for backend
python manage.py runserver
