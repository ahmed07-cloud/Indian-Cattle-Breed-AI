@echo off
title Indian Cattle Breed AI

echo ==========================================
echo       INDIAN CATTLE BREED AI
echo ==========================================
echo.

REM ==============================
REM PROJECT PATHS
REM ==============================

set "PROJECT=C:\Users\Admin\OneDrive\Desktop\hackathon\Indian-Cattle-AI-FB"
set "BACKEND=%PROJECT%\backend"
set "FRONTEND=%PROJECT%\frontend"
set "PYTHON=%BACKEND%\venv\Scripts\python.exe"

echo Project:
echo %PROJECT%
echo.

REM ==============================
REM CHECK PROJECT
REM ==============================

if not exist "%PROJECT%" (
    echo ERROR: Project folder not found!
    echo %PROJECT%
    pause
    exit /b 1
)

REM ==============================
REM CHECK BACKEND
REM ==============================

if not exist "%BACKEND%\server.py" (
    echo ERROR: Backend server.py not found!
    echo Expected:
    echo %BACKEND%\server.py
    echo.
    pause
    exit /b 1
)

if not exist "%PYTHON%" (
    echo ERROR: Backend virtual environment not found!
    echo Expected:
    echo %PYTHON%
    echo.
    pause
    exit /b 1
)

REM ==============================
REM CHECK FRONTEND
REM ==============================

if not exist "%FRONTEND%\package.json" (
    echo ERROR: Frontend package.json not found!
    echo Expected:
    echo %FRONTEND%\package.json
    echo.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo Starting FastAPI Backend
echo ==========================================
echo.

REM Backend accessible from other devices on LAN
start "Indian Cattle AI - Backend" cmd /k "cd /d "%BACKEND%" && "%PYTHON%" -m uvicorn server:app --host 0.0.0.0 --port 8000"

echo Backend starting...
timeout /t 5 /nobreak >nul

echo.
echo ==========================================
echo Starting React Frontend
echo ==========================================
echo.

REM Frontend accessible from other devices on LAN
start "Indian Cattle AI - Frontend" cmd /k "cd /d "%FRONTEND%" && npm.cmd run dev -- --host 0.0.0.0"

echo Frontend starting...
timeout /t 8 /nobreak >nul

echo.
echo ==========================================
echo       INDIAN CATTLE BREED AI STARTED
echo ==========================================
echo.

echo Backend:
echo http://127.0.0.1:8000
echo.

echo Backend LAN:
echo http://10.143.241.151:8000
echo.

echo Frontend:
echo http://localhost:5173
echo.

echo Frontend LAN:
echo http://10.143.241.151:5173
echo.

echo ==========================================
echo.
echo PHONE:
echo http://10.143.241.151:5173
echo.
echo API:
echo http://10.143.241.151:8000/docs
echo.
echo ==========================================
echo.

REM Open website on laptop
start "" "http://localhost:5173"

echo Browser