@REM Actual date tXt file =  create timestamp text file with optional name linux/windows - http://safrm.net/projects/af
@REM author:  Miroslav Safr miroslav.safr@gmail.com

@echo off
 for /f "tokens=2-4 delims=. " %%g in ('date /t') do ( 
  set dd=%%g
  set mm=%%h
  set yy=%%i
  set rest=%%j )
@REM directory
echo "***************************************************"
if [%1]==[] ( START notepad "%yy%_%mm%_%dd%.txt" && echo "%yy%_%mm%_%dd%.txt created" )
if /i [%1] neq []  ( START notepad "%yy%_%mm%_%dd%_%1.txt" && echo "%yy%_%mm%_%dd%_%1.txt created")

