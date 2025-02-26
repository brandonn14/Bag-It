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

@REM Make migrations
py manage.py makemigrations
py manage.py migrate

REM Deactivate virtual environment
echo Deactivating virtual environment...
call %VENV_DIR%\Scripts\deactivate

echo:
echo Done!
echo:

pause