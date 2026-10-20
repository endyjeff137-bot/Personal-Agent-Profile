@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ==========================================
echo   Personal-Agent-Profile - One-click Push
echo ==========================================
echo.
echo [1/3] Staging changes...
git add -A
echo.
echo [2/3] Commit...
set /p MSG=Change note (press Enter for default):
if "%MSG%"=="" set MSG=update profile
git commit -m "%MSG%" || echo (nothing to commit, skip)
echo.
echo [3/3] Pushing to GitHub...
git push origin main
echo.
if errorlevel 1 (
  echo [FAILED] See GITHUB-AUTH.md for troubleshooting.
) else (
  echo [OK] Pushed.
  echo Check: https://github.com/endyjeff137-bot/Personal-Agent-Profile
)
echo.
pause
