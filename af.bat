@REM Actual date Folder =  create timestamp dir with optional name linux/windows - https://github.com/safrm/af
@REM author:  Miroslav Safr miroslav.safr@gmail.com

@echo off
echo creating actual date directory
 for /f "tokens=2-4 delims=. " %%g in ('date /t') do ( 
  set dd=%%g
  set mm=%%h
  set yy=%%i
  set rest=%%j )
@REM directory
echo "***************************************************"
if [%1]==[] ( MD "%yy%_%mm%_%dd%" && echo "%yy%_%mm%_%dd% created")
if /i [%1] neq []  ( MD "%yy%_%mm%_%dd%_%1" && echo "%yy%_%mm%_%dd%_%1 created")

