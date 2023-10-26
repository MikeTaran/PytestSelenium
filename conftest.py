import os.path
import shutil
from datetime import datetime

import allure
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# для корректного отображения кириллицы в параметризаторах
def pytest_make_parametrize_id(config, val): return repr(val)


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")

    parser.addoption('--language', action='store', default='en',
                     help="Choose language: '--language=en' or '--language=ru'")


# это добавит возможность писать параметры в коммандной строке:
# pytest -s -v --browser_name=firefox --language=ru


# добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом) По умолчанию хром
# parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
# Можно задать значение параметра по умолчанию,
# чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:

# Запуск браузера(для каждой функции)
@pytest.fixture(scope="function")  # по умолчанию запускается для каждой функции
def driver(request):
    browser_name = request.config.getoption(
        "browser_name")  # получаем параметр командной строки browser_name
    user_language = request.config.getoption("language")
    driver = None

    if browser_name == "chrome":
        options = Options()
        # options.add_argument('--headless')  # Включение режима headless
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser_name == "firefox":
        options_firefox = OptionsFirefox()
        # options_firefox.add_argument('--headless')  # Включение режима headless
        options_firefox.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options_firefox)
        # driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    driver.quit()


@allure.step('Run make allure report')
def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        # test_name = item.name
        if call.excinfo is not None:
            # status = 'failed'
            # logger.error(f'{status} - {test_name}. Reason: {str(call.excinfo)}')
            try:
                driver = item.funcargs['driver']
                # driver.save_screenshot('allure-results/screenshot.png')
                # allure.attach.file('allure-results/screenshot.png', name='Screenshot',
                #                    attachment_type=allure.attachment_type.PNG)
                attach = driver.get_screenshot_as_png()
                allure.attach(attach, name=f"Screenshot_{datetime.today()}", attachment_type=allure.attachment_type.PNG)

                allure.attach(driver.page_source, name="HTML source", attachment_type=allure.attachment_type.HTML)
            except Exception as e:
                print(f"Failed to take screenshot: {e}")


@allure.step('Clear allure-reports dir')
def pytest_sessionstart(session):
    allure_report_dir = 'allure-results'
    if os.path.exists(allure_report_dir):
        for file_name in os.listdir(allure_report_dir):
            file_path = os.path.join(allure_report_dir, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}). Reason: {e}")

# pip freeze > requirements.txt   Эта команда сохранит все версии пакетов в специальный файл requirements.txt.
# pip install -r requirements.txt  В свежем окружении все пакеты установлены одной командой!
