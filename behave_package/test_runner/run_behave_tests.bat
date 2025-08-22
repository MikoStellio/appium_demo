cd ../../..
call .venv\Scripts\activate.bat

cd appium_demo

behave behave_package/behave/features -o test_reports/behave_report.txt

pause