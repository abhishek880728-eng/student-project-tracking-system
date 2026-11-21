@echo off
title VCET IT - Reset SQLite Database
echo ======================================================================
echo   VCET IT - Student Project & Skill Tracking System (Database Setup)
echo   Student: Abhishek.R (732925ITR002) - Class: 25IT3A
echo ======================================================================
echo.
cd /d "%~dp0"

echo [*] Clearing any stale database locks...
del /f /q "database\tracking_system.db-journal" >nul 2>&1

echo [*] Initializing SQLite database schema and seed records...
python database/setup_database.py

echo.
pause
