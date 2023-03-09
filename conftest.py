''' Configuration file for Pytest module. '''

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.chrome.options import Options as chromeOptions

LANGUAGES = ['ru', 'en', 'fr', 'es']


def pytest_addoption(parser):
    ''' Pars command line options. '''
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help=f'Choose language: {LANGUAGES}')


@pytest.fixture(scope='function')
def browser(request):
    ''' Browser configuration. '''
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        options = chromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print('\nstart chrome browser for test..')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = firefoxOptions()
        options.set_preference('intl.accept_languages', language)
        print('\nstart firefox browser for test..')
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\nquit browser..')
    browser.quit()
