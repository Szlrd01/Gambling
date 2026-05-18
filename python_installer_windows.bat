@echo off
setlocal EnableDelayedExpansion

:: Ellenőrzi hogy van-e Python launcher
where py >nul 2>nul
if %errorlevel% equ 0 goto install_modules

echo Python nincs telepitve. Letoltes...

:: Hivatalos Windows 11 kompatibilis Python installer URL
curl -L -o python_installer.exe https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe

if not exist python_installer.exe (
    echo Nem sikerult letolteni a Python installert.
    pause
    exit /b
)

echo Python telepitese...

:: Csendes telepites PATH-ba rakassal
start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

del python_installer.exe

:: PATH frissites az aktualis sessionre
set "PATH=%LocalAppData%\Programs\Python\Python313\;%LocalAppData%\Programs\Python\Python313\Scripts\;%ProgramFiles%\Python313\;%ProgramFiles%\Python313\Scripts\;%PATH%"

:install_modules

py --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python telepites sikertelen.
    pause
    exit /b
)

echo Pip frissitese...
py -m pip install --upgrade pip

echo Modulok telepitese...
py -m pip install colorama emoji

echo Kesz.
pause