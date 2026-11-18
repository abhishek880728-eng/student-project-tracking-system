@echo off
setlocal
echo ======================================================================
echo  VCET IT - Push to GitHub Repository
echo  Student: Abhishek.R (732925ITR002) - Class: 25IT3A
echo ======================================================================
echo.

cd /d "%~dp0"
set "PATH=%~dp0.tools\bin;%~dp0.tools\git\cmd;%PATH%"

echo [*] Starting GitHub Login...
echo An 8-character code will appear below.
echo Press Enter, enter the code in your browser, and click Authorize!
echo.

gh auth login --hostname github.com --git-protocol https --web

echo.
echo [*] Pushing repository to GitHub...
.tools\git\cmd\git.exe push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ======================================================================
    echo [SUCCESS] 100%% PUSHED TO GITHUB!
    echo Check repository: https://github.com/abhishek880728-eng/student-project-tracking-system
    echo ======================================================================
) else (
    echo [X] Push encountered an issue.
)
pause
