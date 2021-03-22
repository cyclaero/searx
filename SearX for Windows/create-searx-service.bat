@echo off

for /f "tokens=* USEBACKQ" %%a in ( `py -c "import sysconfig; print(sysconfig.get_paths()['scripts']+'\\searx-run.exe')"`) do (
   sc create SearX binpath= "%%a" start= auto
)

pause
