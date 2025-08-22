Feature: Complete a todo
  As a user
  I want to open the todo app and complete a new todo item in my list
  So that I can remember the things I completed doing


  Scenario: User can complete a todo item
    Given App shows an empty todo list

    When  User add a todo list "Buy Groceries"
    And   User complete the "first" item in the todo list

    Then  App shows the "first" item in the todo list is complete
