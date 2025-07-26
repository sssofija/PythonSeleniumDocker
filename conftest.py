import os
import time
import requests
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def wait_for_selenium(url, timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        try:
            response = requests.get(url)
            if response.status_code in (200, 404):
                return
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)

@pytest.fixture(scope="function")
def browser(request):
    selenium_url = os.getenv("SELENIUM_REMOTE_URL", "http://selenium:4444")
    wait_for_selenium(selenium_url)
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=options
    )
    yield driver
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name="screenshot_on_failure",
                      attachment_type=allure.attachment_type.PNG)
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
