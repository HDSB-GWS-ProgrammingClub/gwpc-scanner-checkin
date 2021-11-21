@ECHO OFF

:: Installing requirements
ECHO Installing requirements
CALL py -m pip install -r %CD%\requirements.txt
ECHO Installed requirements

:: Start
ECHO Starting GWPC Check-in 2.0
CALL py %CD%\main.py