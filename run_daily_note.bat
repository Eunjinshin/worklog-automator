@echo off
rem NOTE: Keep this file ASCII-only. cmd.exe reads .bat as the system ANSI
rem codepage (CP949 here), so non-ASCII text saved as UTF-8 breaks parsing.
chcp 65001 > nul

rem Pin the working directory to this batch file's folder.
cd /d "%~dp0"

python daily_note_agent_v2.py
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to run the script. Check that Python is installed.
    pause
)
