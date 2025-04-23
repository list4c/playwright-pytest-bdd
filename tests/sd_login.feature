Feature: User Login

@smoke
Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters username "standard_user" and password "secret_sauce"
    And the user clicks the Login button
    Then the user should be redirected to the product page

@login
Scenario: Login with invalid credentials
    Given the user is on the login page
    When the user enters username "InvalidUser" and password "InvalidPassword"
    And the user clicks the Login button
    Then the user should see an error message
