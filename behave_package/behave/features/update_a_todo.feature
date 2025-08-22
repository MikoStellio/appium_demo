Feature: Update a todo
  As a user
  I want to be able to edit a Todo item in my list to update the items title
  So that I can change or refine the todo item


  Scenario: User can update an incomplete todo item
    Given App shows an empty todo list

    When  User add a todo list "Buy Groceries"
    And   User updates the "first" item in the todo list to "Pay Water Bill"

    Then  App shows "Pay Water Bill" in todo list


  Scenario: User can update a complete todo item
    Given App shows an empty todo list

    When  User add a todo list "Buy Groceries"
    And   User complete the "first" item in the todo list
    And   User updates the "first" item in the todo list to "Pay Water Bill"

    Then  App shows "Pay Water Bill" in todo list
