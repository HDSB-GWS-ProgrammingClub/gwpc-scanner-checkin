@ECHO off

:: Install requirements
ECHO Installing requirements
CALL npm install
CALL pip install -r %CD%\requirements.txt
ECHO Installed requirements

:: Compile
ECHO Compiling TypeScript
CALL npx tsc -p %CD%\tsconfig.json
ECHO Code compiled successfully

:: Start
ECHO Starting GWPC Check-in 2.0
CALL npm start