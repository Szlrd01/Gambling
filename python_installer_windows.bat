@echo off
setlocal enabledelayedexpansion

where py >nul 2>nul
if %errorlevel% equ 0 goto install_modules

curl -L -o python_installer.exe python.org

if not exist python_installer.exe exit

python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
timeout /t 10 >nul
del python_installer.exe

:install_modules
set "PATH=%ProgramFiles%\Python313\;%ProgramFiles%\Python313\Scripts\;%PATH%"

py --version >nul 2>nul
if %errorlevel% neq 0 exit

py -m pip install --upgrade pip
py -m pip install colorama
py -m pip install emoji

pause