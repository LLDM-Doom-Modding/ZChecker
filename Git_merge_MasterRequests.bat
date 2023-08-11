@echo off
setlocal

rem Same as shell's "BRANCHNAME=$(git rev-parse --abbrev-ref HEAD)"
for /F "delims=" %%i in ('git rev-parse --abbrev-ref HEAD') do set BRANCHNAME=%%i

if "%BRANCHNAME%"=="master" goto Merge_into_Master
if "%BRANCHNAME%"=="requests" goto Merge_into_Requests
goto Error


:Merge_into_Requests
git merge --no-ff --no-commit master
git reset HEAD ZScript/Core/ZCBranchSpecific.zsc
git checkout -- ZScript/Core/ZCBranchSpecific.zsc
git commit -m "Merge branch 'master' into requests"
goto End


:Merge_into_Master
git merge --no-ff --no-commit requests
git reset HEAD ZScript/Core/ZCBranchSpecific.zsc
git checkout -- ZScript/Core/ZCBranchSpecific.zsc
git commit -m "Merge branch 'requests' into master"
goto End


:Error
echo Wrong current branch: "%BRANCHNAME%".

:End
echo on
