
@REM Windows install script for the Flyff Universe launcher

@echo off

if not exist ..\venv\ (
   python -m venv ..\venv
   ..\venv\Scripts\pip install -r ..\requirements.txt
)

..\venv\Scripts\python ..\main.py
