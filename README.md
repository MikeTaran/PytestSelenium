#  Автоматизация тестирования Pytest+Selenium


1. Allure:
    * запуск теста: `pytest --alluredir=./allure_reports .\tests\forms_test.py`
    * формирование отчета: `allure serve .\allure_reports\`  
2. Запуск дебаггера через 5сек для DevTools: `setTimeout(() => {debugger;}, 5000)`. 
