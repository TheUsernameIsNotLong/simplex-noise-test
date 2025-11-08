@echo off

SET VENV_DIR=venv

IF NOT EXIST %VENV_DIR% (
    call bin\setup.bat
)

venv\Scripts\python.exe src\main.py
pause