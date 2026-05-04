@echo off
setlocal ENABLEDELAYEDEXPANSION
chcp 65001 >nul

REM 切换到脚本所在目录（video_organizer）
cd /d "%~dp0"

echo [1/4] 检查 Python ...
python --version >nul 2>nul
if errorlevel 1 (
  echo [ERROR] 未检测到 Python，请先安装 Python 3.10+。
  exit /b 1
)

echo [2/4] 检查 PyInstaller ...
python -m PyInstaller --version >nul 2>nul
if errorlevel 1 (
  echo [INFO] 未检测到 PyInstaller，正在安装依赖...
  pip install -r requirements.txt
  if errorlevel 1 (
    echo [ERROR] 依赖安装失败，请检查网络或 pip 配置。
    exit /b 1
  )
)

echo [3/4] 清理旧产物 ...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist video_organizer.spec del /f /q video_organizer.spec

echo [4/4] 开始打包 EXE ...
python -m PyInstaller ^
  --noconfirm ^
  --clean ^
  --onefile ^
  --windowed ^
  --name video_organizer ^
  --paths . ^
  --collect-submodules app ^
  main.py

if errorlevel 1 (
  echo [ERROR] 打包失败。
  exit /b 1
)

echo [OK] 打包完成：%CD%\dist\video_organizer.exe
exit /b 0
