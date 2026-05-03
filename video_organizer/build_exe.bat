@echo off
setlocal

REM 使用 PyInstaller 打包 video_organizer/main.py
pyinstaller --noconfirm --onefile --windowed --name video_organizer main.py

echo Build finished.
pause
