cd ../../..
call .venv\Scripts\activate.bat

behave appium_demo/behave_package/behave/features -o test_reports/behave_report.txt

pause