@echo off
reg query "hkcu\software\Python"
if ERRORLEVEL 1 GOTO NOPYTHON
GOTO PYTHON
:NOPYTHON
echo You have to install python to run this application

:PYTHON
echo [Installing] Django
pip install django
echo [Done] 
echo [Installing] geopy
pip install geopy
echo [Done]
pause

