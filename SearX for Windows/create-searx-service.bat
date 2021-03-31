@echo off

for /f "tokens=* USEBACKQ" %%a in ( `py -c "import sysconfig; print(sysconfig.get_paths()['scripts']+'\\searx-run.exe')"`) do (
   sc create SearX binpath= "%%a" start= auto
)

reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /f /v SEARX_SETTINGS_PATH /t REG_SZ /d "C:\Users\Public\searx-settings.yml"

pause
