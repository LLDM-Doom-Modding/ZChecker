@echo off
setlocal

FOR /F "delims=" %%i IN ('git rev-parse --abbrev-ref HEAD') DO set BRANCHNAME=%%i


if "%BRANCHNAME%"=="master" goto Merge_into_Master
if "%BRANCHNAME%"=="requests" goto Merge_into_Requests
goto Error

:Merge_into_Requests
git merge --no-ff --no-commit master
git reset HEAD ZScript/ZCBranchSpecific.zsc
git checkout -- ZScript/ZCBranchSpecific.zsc
git commit -m "Merge branch 'master' into requests"
goto End


:Merge_into_Master
git merge --no-ff --no-commit requests
git reset HEAD ZScript/ZCBranchSpecific.zsc
git checkout -- ZScript/ZCBranchSpecific.zsc
git commit -m "Merge branch 'requests' into master"
goto End


:Error
echo Wrong current branch: "%BRANCHNAME%".

:End
echo on
