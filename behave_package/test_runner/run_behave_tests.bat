cd ../../..
call .venv\Scripts\activate.bat

cd appium_demo

behave behave_package/behave/features

pause