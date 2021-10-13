@echo off

:: Python virtual environment
echo "Created and activated Python virtual environment"
py -m venv %CD%\venv
source %CD%\venv\bin\activate

:: Install requirements
npm install
pip install -r %CD%\requirements.txt
echo "Installed requirements"

:: Compile
tsc -p %CD%\tsconfig.json
echo "Code compiled successfully"

:: Start
echo "Starting GWPC Check-in 2.0"
npm start