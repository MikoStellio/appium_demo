Feature: Add a todo
  As a user
  I want to  see that todo item length is limited to a maximum of 200 characters
  So that I can limit the characters of the title of my todo


  Scenario: User can type a 1 character todo item
    Given App shows an empty todo list

    When  User set a "1" character in the todo list textbox

    Then  App shows "199" characters left


  Scenario: User can type a 100 character todo item
    Given App shows an empty todo list

    When  User set a "100" character in the todo list textbox

    Then  App shows "100" characters left


  Scenario: User can type a 200 character todo item
    Given App shows an empty todo list

    When  User set a "200" character in the todo list textbox

    Then  App shows "0" characters left
