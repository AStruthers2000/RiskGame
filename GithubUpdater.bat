@echo off
git add .
set /p CommitMessage=Enter commit message: 
git commit -m "%CommitMessage%"
git push
echo Done
pause