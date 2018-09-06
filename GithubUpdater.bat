@echo off
git add .
set /p CommitMessage=Enter some text: 
git commit -m "%CommitMessage%"
git push
echo "Done"