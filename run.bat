@echo off
chcp 65001 > nul
title Atria: Cyber-Nexus - 启动器
echo ============================================================
echo   Atria: Cyber-Nexus (全息量子智算星网)
echo   正在启动本地环境...
echo ============================================================

REM 检查是否有 Python
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [*] 检测到 Python 环境，正在通过 server.py 启动...
    python server.py
) else (
    echo [!] 未检测到 Python，正在直接通过默认浏览器打开 index.html...
    start "" "%~dp0index.html"
)

pause
