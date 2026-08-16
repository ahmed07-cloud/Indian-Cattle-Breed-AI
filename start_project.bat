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

echo Project:
echo %PROJECT%
echo.

REM ==============================
REM CHECK BACKEND
REM ==============================

if not exist "%BACKEND%\app\main.py" (
    echo ERROR: Backend app\main.py not found!
    echo.
    pause
    exit /b
)

if not exist "%BACKEND%\venv\Scripts\python.exe" (
    echo ERROR: Backend virtual environment not found!
    echo Expected:
    echo %BACKEND%\venv\Scripts\python.exe
    echo.
    pause
    exit /b
)

REM ==============================
REM CHECK FRONTEND
REM ==============================

if not exist "%FRONTEND%\package.json" (
    echo ERROR: Frontend package.json not found!
    echo.
    pause
    exit /b
)

echo.
echo Starting FastAPI Backend...
echo.

start "Indian Cattle AI - Backend" cmd /k "cd /d "%BACKEND%" && "%BACKEND%\venv\Scripts\python.exe" -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000"

echo Backend starting...
timeout /t 5 /nobreak >nul

echo.
echo Starting React Frontend...
echo.

start "Indian Cattle AI - Frontend" cmd /k "cd /d "%FRONTEND%" && npm.cmd run dev -- --host 127.0.0.1"

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
echo Frontend:
echo http://localhost:5173
echo.
echo ==========================================
echo.

start "" "http://localhost:5173"

echo Browser opened.
echo.
echo Keep the Backend and Frontend terminal windows open.
echo.
pause