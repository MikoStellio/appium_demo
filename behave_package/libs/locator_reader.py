import json, os


class LocatorReader:
    def __init__(self, config_file='mobile_element_locators.json'):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        config_path = os.path.join(base_dir, 'configs', config_file)

        with open(config_path) as f:
            self.locators = json.load(f)

    def get_locator(self, locator):
        return self.locators.get(locator)
