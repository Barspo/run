@echo off
REM One-time installation for Windows. Just double-click this file.
setlocal
cd /d "%~dp0"

echo ============================================
echo   Running Coach - Setup
echo ============================================
echo.

REM Prefer the "py" launcher; fall back to "python" on PATH.
set "PY="
where py >nul 2>&1 && set "PY=py -3"
if not defined PY (
  where python >nul 2>&1 && set "PY=python"
)
if not defined PY goto :nopython

echo [1/3] Checking Python...
%PY% --version
if errorlevel 1 goto :nopython

echo.
echo [2/3] Creating virtual environment...
%PY% -m venv .venv
if errorlevel 1 goto :fail

echo.
echo [3/3] Installing packages (this takes a minute)...
".venv\Scripts\python.exe" -m pip install --quiet --upgrade pip
".venv\Scripts\python.exe" -m pip install --quiet -r requirements.txt
if errorlevel 1 goto :fail

echo.
echo ============================================
echo   Setup complete.
echo   Now double-click:  run.bat
echo ============================================
echo.
pause
exit /b 0

:nopython
echo.
echo ERROR: Python was not found on this computer.
echo.
echo 1. Download it from:  https://www.python.org/downloads/
echo 2. During installation, TICK the box "Add Python to PATH"
echo 3. Restart this window and run setup.bat again
echo.
pause
exit /b 1

:fail
echo.
echo ERROR: Setup failed. Copy the message above into the chat.
echo.
pause
exit /b 1
