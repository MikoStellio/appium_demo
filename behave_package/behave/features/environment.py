from behave_package.libs.driver_manager import DriverManager
from behave_package.libs.mobile_automator import MobileAutomator
from behave_package.libs.my_product import MyProduct


def before_all(context):
    print('-----------------BEFORE ALL-----------------')
    context.dm = DriverManager()
    context.p = MyProduct()


def before_scenario(context, scenario):
    print('-----------------BEFORE SCENARIO-----------------')
    context.p.install_app()
    context.dm.start_appium_server()
    context.p.start_streaming()
    context.driver = context.dm.setup_driver()
    context.action = MobileAutomator(context.driver)
    context.total_todo_items = 0


def after_scenario(context, scenario):
    print('-----------------AFTER SCENARIO-----------------')
    context.p.uninstall_app()
    context.dm.stop_appium_server()
    context.p.stop_streaming()


def after_all(context):
    print('-----------------AFTER ALL-----------------')
    if hasattr(context, 'driver'):
        context.driver.quit()