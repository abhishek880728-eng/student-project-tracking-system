@echo off
title VCET IT - Student Project & Skill Tracking System
echo ======================================================================
echo   VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY (AUTONOMOUS)
echo   Department of Information Technology - Class: 25IT3A
echo   Author: Abhishek.R (732925ITR002) - Scenario 2
echo ======================================================================
echo.
cd /d "%~dp0"

echo [*] Ensuring port 8080 is clear...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8080') do (
    taskkill /F /PID %%a >nul 2>&1
)

echo [*] Launching High-Speed Multi-Threaded Web Server at http://localhost:8080 ...
python web/server.py
pause
