@echo off
echo ======================================================================
echo  VCET IT - Compiling Student Project & Skill Tracking System (Java)
echo  Student: Abhishek.R (732925ITR002) - Class: 25IT3A
echo ======================================================================

if not exist bin mkdir bin

javac -cp "lib/*" -d bin src/com/vcet/tracking/model/*.java src/com/vcet/tracking/dao/*.java src/com/vcet/tracking/service/*.java src/com/vcet/tracking/*.java

if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Compilation finished successfully. Class files placed in /bin.
) else (
    echo [ERROR] Compilation failed. Please check your JDK installation.
)
pause
