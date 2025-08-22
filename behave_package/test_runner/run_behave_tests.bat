cd ../../..
call .venv\Scripts\activate.bat

cd appium_demo/behave_package

behave behave/features -o test_reports/behave_report.txt

pause