@echo off
REM Kidney Biopsy Report Generator - Launcher
REM This script launches the interactive report generator

cd /d "g:\dr_vinita\xml convert"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    echo Please install Python or add it to your PATH
    pause
    exit /b 1
)

REM Launch the application
echo Launching Kidney Biopsy Report Generator...
python kidney_biopsy_report_generator.py

if errorlevel 1 (
    echo An error occurred while running the application
    pause
)
