:: A beautifier for the user

@echo off
cls

:main
echo You want to open :
echo 1: Python file
echo 2: Executable file
set choice =
set /p choice=

if '%choice%'=='1' goto python
if '%choice%'=='2' goto executable
echo Please enter a valid choice
echo
goto main

:python
echo Starting Python script
start "Cryptography Project" Python/main.py [/B]
goto end

:executable
echo Starting Executable script
start "Cryptography Project" Executable/main.exe [/B]
goto end

:end
exit
