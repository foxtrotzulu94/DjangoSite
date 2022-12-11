@ECHO OFF
set EnvName=DEV-ENV-WIN

python -m virtualenv %EnvName%
call %EnvName%\Scripts\activate.bat
pip install -r requirements.txt
set DEBUG=True
echo Virtual environment is up and ready to use
pause