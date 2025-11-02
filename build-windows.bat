@echo off
echo Building YouTube Audio Downloader for Windows...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
pip install pyinstaller

REM Check if ffmpeg is available
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo WARNING: ffmpeg not found in PATH
    echo The executable will still work but users will need ffmpeg installed
    echo You can install ffmpeg from: https://ffmpeg.org/download.html
    echo.
)

REM Build the executable
echo Building executable...
pyinstaller --onefile --name youtube-audio-downloader.exe youtube_audio_downloader.py

if exist "dist\youtube-audio-downloader.exe" (
    echo.
    echo SUCCESS: Executable created at dist\youtube-audio-downloader.exe
    echo File size:
    dir "dist\youtube-audio-downloader.exe" | find "youtube-audio-downloader.exe"
    echo.
    echo You can now distribute dist\youtube-audio-downloader.exe to Windows users
) else (
    echo ERROR: Failed to create executable
)

pause
