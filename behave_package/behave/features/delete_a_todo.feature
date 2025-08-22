Feature: Delete a todo
  As a user
  I want to be able to delete a todo item from my list
  So that it is removed


  Scenario: User can delete an incomplete todo item
    Given App shows an empty todo list

    When  User add a todo list "Buy Groceries"
    And   User deletes the "first" item in todo list

    Then  App shows an empty todo list


  Scenario: User can delete a complete todo item
    Given App shows an empty todo list

    When  User add a todo list "Buy Groceries"
    And   User complete the "first" item in the todo list
    And   User deletes the "first" item in todo list

    Then  App shows an empty todo list


  Scenario: User can delete two todo items
    Given App shows an empty todo list

    When  User add a todo list "Buy Groceries"
    And   User add a todo list "Buy Groceries"
    And   User complete the "second" item in the todo list
    And   User deletes the "second" item in todo list
    And   User deletes the "first" item in todo list

    Then  App shows an empty todo list
