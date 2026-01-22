Feature: Login Feature
  @sanity
  Scenario: Successful login
    Given user opens the login page
    When user enters username and password
    Then user should be logged in
