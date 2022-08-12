@ echo off
%1 %2
ver|find "5.">nul&&goto :Admin
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :Admin","","runas",1)(window.close)&goto :eof
:Admin
echo start reg  ...
reg delete HKEY_CLASSES_ROOT\*\shell\double_zip /f >nul 2>&1 && echo 注册表删除成功 || echo 注册表删除失败
reg delete HKEY_CLASSES_ROOT\Directory\shell\double_zip /f >nul 2>&1 && echo 注册表删除成功 || echo 注册表删除失败
pause
@echo on
