@echo off
echo Starting College Enquiry Chatbot...
echo.

:: Navigate to backend and start in a new window
echo [1/2] Starting Backend Server...
start "Chatbot Backend" cmd /k "cd /d d:\Prabhakar\MINI Project\backend && python app.py"

:: Wait a few seconds for server to initialize
timeout /t 3 /nobreak > nul

:: Open the frontend in the default browser
echo [2/2] Opening Frontend...
start "" "http://127.0.0.1:5000/"

echo.
echo All systems started! You can close this window.
pause
