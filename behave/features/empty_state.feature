Feature: Empty state
  As a user
  I want to see a valid empty state screen when there are no todo items added
  So that I know I have nothing todo items anymore


  Scenario: User can see empty list after deleting a todo item
    Given App shows an empty todo list

    When  User add a todo list "Buy Groceries"
    And   User deletes the "first" item in todo list

    Then  App shows an empty todo list
