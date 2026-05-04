@echo off
setlocal ENABLEDELAYEDEXPANSION
chcp 65001 >nul

REM 切换到脚本所在目录（video_organizer）
cd /d "%~dp0"

where pyinstaller >nul 2>nul
if errorlevel 1 (
  echo [ERROR] 未检测到 pyinstaller，请先执行：
  echo         pip install -r requirements.txt
  exit /b 1
)

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist video_organizer.spec del /f /q video_organizer.spec

pyinstaller ^
  --noconfirm ^
  --clean ^
  --onefile ^
  --windowed ^
  --name video_organizer ^
  --paths . ^
  main.py

if errorlevel 1 (
  echo [ERROR] 打包失败。
  exit /b 1
)

echo [OK] 打包完成：%CD%\dist\video_organizer.exe
exit /b 0

