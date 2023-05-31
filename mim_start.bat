@echo off
set PYTHONPATH=%PYTHONPATH%;%~dp0\..;%~dp0
set PATH=C:\Users\patri\AppData\Local\Programs\Python\Python310;%PATH%
@REM set PATH=C:\Users\maya\applications\python_3.7.7;%PATH%

python.exe "%~dp0tools\tray\tray.py" %*

timeout /t 10 /nobreak