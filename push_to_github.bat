@echo off
setlocal
echo ======================================================================
echo  VCET IT - Push to GitHub Repository
echo  Project: Student Project and Skill Tracking System
echo  Student: Abhishek.R (732925ITR002) - Class: 25IT3A
echo  Repo: https://github.com/abhishek880728-eng/student-project-tracking-system.git
echo ======================================================================
echo.

cd /d "%~dp0"
set "PATH=%~dp0.tools\git\cmd;%~dp0.tools\gcm;%PATH%"
set GIT_EXE="%~dp0.tools\git\cmd\git.exe"

echo [*] Launching push with GitHub Browser Sign-In...
echo [!] When the GitHub window pops up, click "Sign in with your browser" and click "Authorize".
echo.

%GIT_EXE% push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ======================================================================
    echo [SUCCESS] PUSH COMPLETED 100%%!
    echo Check your repository: https://github.com/abhishek880728-eng/student-project-tracking-system
    echo ======================================================================
) else (
    echo.
    echo [!] If browser sign-in was not completed, you can enter a Personal Access Token below:
    set /p TOKEN="Paste your GitHub Personal Access Token (or press Enter to exit): "
    if not "%TOKEN%"=="" (
        %GIT_EXE% remote set-url origin https://abhishek880728-eng:%TOKEN%@github.com/abhishek880728-eng/student-project-tracking-system.git
        %GIT_EXE% push -u origin main
        %GIT_EXE% remote set-url origin https://github.com/abhishek880728-eng/student-project-tracking-system.git
    )
)

pause
