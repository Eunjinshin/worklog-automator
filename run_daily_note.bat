@echo off
chcp 65001 > nul
rem 작업 디렉토리를 이 배치 파일이 있는 폴더로 고정 (업무일지 폴더 위치 보장)
cd /d "%~dp0"

python daily_note_agent_v2.py
if errorlevel 1 (
    echo.
    echo [오류] 스크립트 실행에 실패했습니다. Python 설치 여부를 확인하세요.
    pause
)
