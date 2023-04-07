""" Configuration file for Pytest module. """

import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

LANGUAGES = ['ru', 'en', 'fr', 'es']


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    cur_datetime = datetime.today().strftime('%Y%m%d%H%M%S')
    config.option.htmlpath = os.path.join('test_project/', 'logs/', f'report_{cur_datetime}.html')
    config.option.self_contained_html = True


def pytest_addoption(parser):
    """ Pars command line options. """
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help=f'Choose language: {LANGUAGES}')


@pytest.fixture(scope='function')
def browser(request):
    """ Browser configuration. """
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        options = chromeOptions()
        # headless setup, comment if you need to see a browser window!
        options.add_argument("--headless=new")
        options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        options.add_argument("--no-sandbox")  # Bypass OS security model
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        capabilities = browser.capabilities
        print(f'\nstart chrome browser {capabilities["browserVersion"]} for test..')
    elif browser_name == 'firefox':
        # windows setup
        """
        options = firefoxOptions()
        # headless setup, comment if you neeed to see a browser window!
        options.add_argument("-headless")
        options.set_preference('intl.accept_languages', language)
        print('\nstart firefox browser for test..')
        browser = webdriver.Firefox(options=options)
        """
        # linux setup
        """
        install_dir = "/snap/firefox/current/usr/lib/firefox"
        driver_loc = os.path.join(install_dir, "geckodriver")
        binary_loc = os.path.join(install_dir, "firefox")
        """

        # container setup
        driver_loc = "/usr/local/bin/geckodriver"
        binary_loc = "/usr/lib/firefox/firefox"

        # linux setup
        service = FirefoxService(driver_loc)
        options = webdriver.FirefoxOptions()
        options.binary_location = binary_loc
        # headless setup, comment if you need to see a browser window!
        options.add_argument("-headless")
        options.set_preference('intl.accept_languages', language)

        print('\nstart firefox browser for test..')
        browser = webdriver.Firefox(service=service, options=options)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\nquit browser..')
    browser.quit()
