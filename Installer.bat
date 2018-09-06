@echo off
cd ..
echo rmdir /s /q RiskGame && git clone "https://github.com/Computer-Nerd123/RiskGame.git" >> Installer.bat
start Installer.bat
pause