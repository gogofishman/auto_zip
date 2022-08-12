@ echo off
%1 %2
ver|find "5.">nul&&goto :Admin
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :Admin","","runas",1)(window.close)&goto :eof
:Admin
echo start reg  ...
reg add HKEY_CLASSES_ROOT\*\shell\double_zip /ve /t REG_SZ /d "一键打包成双层zip" /f
reg add HKEY_CLASSES_ROOT\*\shell\double_zip\command /ve /t REG_SZ /d "\"%~dp0auto_zip.exe\" \"%%1\"" /f
pause
@echo on
