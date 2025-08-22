import json, os, time, subprocess
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService


class DriverManager:
    def __init__(self, config_file="android_app_config.json"):
        self.driver = None
        self.appium_service = AppiumService()
        base_dir = os.path.dirname(os.path.dirname(__file__))
        config_path = os.path.join(base_dir, 'configs', config_file)

        with open(config_path) as f:
            self.capabilities = json.load(f)

    def setup_driver(self):
        options_caps = UiAutomator2Options().load_capabilities(self.capabilities)
        try:
            self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options_caps)
        except Exception as e:
            print(f'Failed to setup driver: {e}')
            print('Restarting webdriver...')
            self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options_caps)
        return self.driver

    def start_appium_server(self):
        self.appium_service.start(args=['-p 4723'])
        time.sleep(5) # Wait for appium server to initialize

    def stop_appium_server(self):
        self.appium_service.stop()
