from behave import *
import time, re


#############
#   STEP    #
#############
@step('App shows an empty todo list')
def step_impl(context):
    return_element_status = context.action.verify_element_present(context.driver, 'HOME_EMPTYLIST_LABEL', 30)
    if not return_element_status:
        assert False


@step('User add a todo list "{text}"')
def step_impl(context, text):
    context.total_todo_items += 1
    return_element_status = context.action.set_text(context.driver, 'HOME_TODOITEM_TEXTBOX', text, 10)
    if not return_element_status:
        assert False
    return_element_status = context.action.tap_element(context.driver, 'HOME_ADD_BUTTON')
    if not return_element_status:
        assert False


#############
#   WHEN    #
#############
@when('App is relaunched')
def step_impl(context):
    context.action.terminate_app()
    time.sleep(2)
    context.action.launch_app()


@when('User complete the "{count}" item in the todo list')
def step_impl(context, count):
    time.sleep(2)
    item_in_list = {
        'first': 'HOME_FIRSTTODOLIST_CHECKBOX',
        'second': 'HOME_SECONDTODOLIST_CHECKBOX'
    }
    return_element_status = context.action.tap_element(context.driver, item_in_list.get(count))
    if not return_element_status:
        assert False


@when('User deletes the "{count}" item in todo list')
def step_impl(context, count):
    item_in_list = {
        'first': 'HOME_FIRSTTODODELETE_BUTTON',
        'second': 'HOME_SECONDTODODELETE_BUTTON'
    }
    return_element_status = context.action.tap_element(context.driver, item_in_list.get(count))
    if not return_element_status:
        assert False


@when('User updates the "{count}" item in the todo list to "{text}"')
def step_impl(context, count, text):
    item_in_list = {
        'first': 'HOME_FIRSTTODOEDIT_BUTTON',
        'second': 'HOME_SECONDTODOEDIT_BUTTON'
    }
    return_element_status = context.action.tap_element(context.driver, item_in_list.get(count))
    if not return_element_status:
        assert False
    return_element_status = context.action.set_text(context.driver, 'HOME_TODOEDITITEM_TEXTBOX', text)
    if not return_element_status:
        assert False
    return_element_status = context.action.tap_element(context.driver, 'HOME_SAVEEDIT_BUTTON')
    if not return_element_status:
        assert False


@when('User set a "{count}" character in the todo list textbox')
def step_impl(context, count):
    text_to_input = 'a' * int(count)
    return_element_status = context.action.set_text(context.driver, 'HOME_TODOITEM_TEXTBOX', text_to_input, 10)
    if not return_element_status:
        assert False


@when('User add "{count}" items in todo list')
def step_impl(context, count):
    count = int(count)
    for n in range(count):
        context.execute_steps(f'''when User add a todo list "a"''')
        time.sleep(3)


#############
#   THEN    #
#############
@then('App shows "{count}" item/s in todo list')
def step_impl(context, count):
    return_element_count = context.action.get_content_id(context.driver, 'HOME_LISTCOUNTER_LABEL')
    if not return_element_count:
        assert False
    get_digits = re.search(r'\d+', return_element_count)
    get_digits = int(get_digits.group())
    print(f'Comparing "{count}" with app\'s actual label: "{get_digits}"')
    assert int(count) == get_digits and int(count) == context.total_todo_items


@then('App shows "{item}" in todo list')
def step_impl(context, item):
    if not hasattr(context, 'element_locator'):
        context.element_locator = 'HOME_TODOLIST_LABEL'
        context.string_to_replace = 'todo-text-0\n'
    return_element_label = context.action.get_content_id(context.driver, context.element_locator)
    if not return_element_label:
        assert False
    get_element_text = return_element_label.replace(context.string_to_replace, '')
    print(f'Comparing "{item}" with app\'s actual label: "{get_element_text}"')
    assert item == get_element_text


@then('App shows second item as "{item}" in todo list')
def step_impl(context, item):
    context.element_locator = 'HOME_SECONDTODOLIST_LABEL'
    context.string_to_replace = 'todo-text-1\n'
    context.execute_steps(f'''then App shows "{item}" in todo list''')
    del context.element_locator
    del context.string_to_replace


@then('App shows the "{count}" item in the todo list is complete')
def step_impl(context, count):
    item_in_list = {
        'first': 'HOME_FIRSTTODOLIST_CHECKBOX',
        'second': 'HOME_SECONDTODOLIST_CHECKBOX'
    }
    return_element_status = context.action.verify_element_ticked(context.driver, item_in_list.get(count))
    if not return_element_status:
        assert False


@then('App shows "{count}" characters left')
def step_impl(context, count):
    maximum_character_label = 'No characters remaining'
    return_element_label = context.action.get_content_id(context.driver, 'HOME_CHARACTERSLEFT_LABEL')
    if not return_element_label:
        assert False

    if 200 >= int(count) > 0:
        get_digits = re.search(r'\d+', return_element_label)
        get_digits = int(get_digits.group())
        assert int(count) == get_digits
    elif int(count) == 0:
        assert maximum_character_label == return_element_label
    else:
        assert False, f'"{count}" not within expected count'
