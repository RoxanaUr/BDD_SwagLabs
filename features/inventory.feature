Feature: Inventory Page

  Scenario: Has 6 products on page
    Given I am on the Sign in page
    When I login successfully with "standard_user" and "secret_sauce"
    Then There are 6 product on the Inventory page

  @single
  Scenario: Redirect to Login page when unauthenticated user
    Given I am not a logged in user
    When I try to access the Inventory page
    Then I am redirected to Login page
    And I receive a Epic sadface error message