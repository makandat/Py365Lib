@echo off
robocopy /s C:\workspace\Scripts\python3\Py365Lib C:\workspace\GitHub\Py365Lib
del Py365Lib.log
xcopy /d C:\workspace\Scripts\python3\HTApp\HTApp.py C:\workspace\GitHub\Py365Lib\HTApp.py
xcopy /d C:\workspace\Scripts\python3\TkApp\TkApp.py C:\workspace\GitHub\Py365Lib\TkApp.py
xcopy /d C:\workspace\Scripts\python3\CursesApp\CursesApp.py C:\workspace\GitHub\Py365Lib\CursesApp.py

rem WebPage
xcopy /d /s "C:\workspace\Linux\Inspiron570 (Ubuntu 18.04LTS)\cgi-bin\Py365Lib\*.*" C:\workspace\GitHub\Py365Lib\test\WebPage

rem CursesApp
xcopy /d C:\workspace\Scripts\python3\CursesApp\test\*.* C:\workspace\GitHub\Py365Lib\test\CursesApp
xcopy /d C:\workspace\Scripts\python3\CursesApp\utilities\*.* C:\workspace\GitHub\Py365Lib\utilities\CursesApp

rem TkApp
xcopy /d C:\workspace\Scripts\python3\TkApp\test\*.* C:\workspace\GitHub\Py365Lib\test\TkApp
xcopy /d C:\workspace\Scripts\python3\TkApp\utilities\*.* C:\workspace\GitHub\Py365Lib\utilities\TkApp

rem HTApp
xcopy /d C:\workspace\Scripts\python3\HTApp\test\*.* C:\workspace\GitHub\Py365Lib\test\HTApp
xcopy /d C:\workspace\Scripts\python3\HTApp\test\html\*.* C:\workspace\GitHub\Py365Lib\test\HTApp\html
xcopy /d C:\workspace\Scripts\python3\HTApp\test\templates\*.* C:\workspace\GitHub\Py365Lib\test\HTApp\templates
pause
