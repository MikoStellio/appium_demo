cd ..
call .venv\Scripts\activate.bat

behave behave/features -o test_reports/behave_report.txt

pause