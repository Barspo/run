@echo off
REM Pull data from Garmin and build the report. Double-click to run.
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo.
  echo Environment not installed yet.
  echo Double-click setup.bat first, then come back here.
  echo.
  pause
  exit /b 1
)

".venv\Scripts\python.exe" coach.py %*
if errorlevel 1 goto :fail

echo.
echo ============================================
echo   Report ready:  data\coach_report.md
echo   Open it, copy everything,
echo   and paste it into the chat.
echo ============================================
echo.
pause
exit /b 0

:fail
echo.
echo Something went wrong. Copy the message above into the chat.
echo.
pause
exit /b 1
