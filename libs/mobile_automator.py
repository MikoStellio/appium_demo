import time
from bdb import effective

from libs.locator_reader import LocatorReader
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MobileAutomator:
    def __init__(self, driver, default_timeout=5):
        self.driver = driver
        self.default_timeout = default_timeout
        self.locator_reader = LocatorReader()

    def _set_timeout(self, timeout):
        return self.default_timeout if timeout is None else timeout

    def get_element(self, driver, locator, timeout=None):
        effective_timeout = self._set_timeout(timeout)
        element = self.locator_reader.get_locator(locator)
        try:
            if 'id' in element:
                element = WebDriverWait(driver, effective_timeout).until(
                        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, element.get('id')))
                )
            elif 'xpath' in element:
                element = WebDriverWait(driver, effective_timeout).until(
                    EC.visibility_of_element_located((AppiumBy.XPATH, element.get('xpath')))
                )
            else:
                return NoSuchElementException()
        except Exception as e:
            print(f'Element "{locator}" was not found, error raised: {e}')
            raise AssertionError()
        return element

    def launch_app(self, app_package=None, app_activity=None, target_activity=None, timeout=None):
        effective_timeout = self._set_timeout(timeout)
        if app_activity is None:
            app_activity = self.driver.capabilities.get('appActivity')
            target_activity = app_activity
        if app_package is None:
            app_package = self.driver.capabilities.get('appPackage')

        self.driver.activate_app(app_package)
        if target_activity:
            WebDriverWait(self.driver, 15).until(
                lambda d: target_activity == app_activity
            )

    def terminate_app(self, app=None):
        if app is None:
            app = self.driver.capabilities.get('appPackage')
        self.driver.terminate_app(app)

    def verify_element_present(self, driver, locator, timeout=None):
        effective_timeout = self._set_timeout(timeout)
        return_element_state = self.get_element(driver, locator, effective_timeout)
        if return_element_state:
            return True
        else:
            raise AssertionError(f'Element "{locator}" not found')

    def tap_element(self, driver, locator, timeout=None):
        effective_timeout = self._set_timeout(timeout)
        element = self.locator_reader.get_locator(locator)
        if 'id' in element:
            element = WebDriverWait(driver, effective_timeout).until(
                    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, element['id']))
            )
        elif 'xpath' in element:
            element = WebDriverWait(driver, effective_timeout).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, element['xpath']))
            )
        else:
            raise NoSuchElementException()
        element.click()
        return True

    def set_text(self, driver, locator, text, timeout=None):
        effective_timeout = self._set_timeout(timeout)
        element = self.get_element(driver, locator, effective_timeout)
        self.tap_element(driver, locator, effective_timeout)
        if element:
            print(f'Setting {text} to {element}')
            element.clear()
            element.send_keys(text)
            return True
        else:
            return False

    def get_text(self, driver, locator, timeout=None):
        effective_timeout = self._set_timeout(timeout)
        element = self.get_element(driver, locator, effective_timeout)
        if element:
            if element.text:
                return element.text
            elif element.get_attribute('text'):
                return element.get_attribute('text')
            else:
                return False
        else:
            return False

    def get_content_id(self, driver, locator, timeout=None):
        effective_timeout = self._set_timeout(timeout)
        element = self.get_element(driver, locator, effective_timeout)
        if element:
            return element.get_attribute('content-desc')
        else:
            return False

    def verify_element_ticked(self, driver, locator, timeout = None):
        effective_timeout = self._set_timeout(timeout)
        element = self.get_element(driver, locator, effective_timeout)
        element_status = element.get_attribute('checked')
        return element_status
