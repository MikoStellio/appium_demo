Feature: Item count
  As a user
  I want to see an accurate count of how many total todo items are in my list
  So that I can see how many todo items I have listed


  Scenario: App shows exact count of items in todo list when 1 item is added
    Given App shows an empty todo list

    When  User add a todo list "Buy Groceries"

    Then  App shows "1" item/s in todo list


  Scenario: App shows exact count of items in todo list when 2 items are added
    Given App shows an empty todo list

    When  User add a todo list "Buy Groceries"
    And   User add a todo list "Pay Water Bill"

    Then  App shows "2" item/s in todo list


  Scenario: App shows exact count of items in todo list when 8 items are added
    Given App shows an empty todo list

    When  User add "8" items in todo list

    Then  App shows "8" item/s in todo list
