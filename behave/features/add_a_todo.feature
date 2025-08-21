Feature: Add a todo
  As a user
  I want to open the todo app and add a new todo item
  So that I can remember the things I need to do


  Scenario: User can add a todo item
    Given App shows an empty todo list

    When  User add a todo list "Buy Groceries"

    Then  App shows "1" item/s in todo list
    And   App shows "Buy Groceries" in todo list


  Scenario: App retains todo items after app relaunch
    Given App shows an empty todo list

    When  User add a todo list "Buy Groceries"
    And   App is relaunched

    Then  App shows "1" item/s in todo list
    And   App shows "Buy Groceries" in todo list


  Scenario: App shows multiple entries in todo list
    Given App shows an empty todo list

    When  User add a todo list "Buy Groceries"
    And   User add a todo list "Pay Water Bill"

    Then  App shows "2" item/s in todo list
    And   App shows "Buy Groceries" in todo list
    And   App shows second item as "Pay Water Bill" in todo list


  Scenario: User can add an item in Japanese
    Given App shows an empty todo list

    When  User add a todo list "食料品を買う"

    Then  App shows "1" item/s in todo list
    And   App shows "食料品を買う" in todo list
