@echo off

REM Set the path to the virtual environment
set VENV_DIR=env

REM Check if the virtual environment exists
if not exist %VENV_DIR% (
    @REM echo Virtual environment not found! Creating one...
    call init.bat
)

REM Activate the virtual environment
call %VENV_DIR%\Scripts\activate

py ./manage.py runserver
