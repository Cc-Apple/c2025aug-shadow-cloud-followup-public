@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ============================================================
echo Verify Remaining Five-System Public Pack
echo ============================================================
echo.

python verify_remaining_five_public_pack.py

echo.
echo ============================================================
echo Output:
echo VERIFY_REPORT.json
echo VERIFY_REPORT.csv
echo ============================================================
pause