@echo off
REM Set the path to the virtual environment
set VENV_DIR=env

REM Check if the virtual environment exists
if not exist %VENV_DIR% (
    echo Virtual environment not found! Creating one...
    python -m venv %VENV_DIR%
)

REM Activate the virtual environment
call %VENV_DIR%\Scripts\activate

REM Install requirements
if exist requirements.txt (
    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt
) else (
    echo requirements.txt not found!
)

REM Deactivate virtual environment
echo Deactivating virtual environment...
call %VENV_DIR%\Scripts\deactivate

echo:
echo Done!
echo:

pause