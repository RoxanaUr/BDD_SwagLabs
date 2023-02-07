Feature: Inventory Page

  Scenario: Has 6 products on page
    Given I am on the Sign in page
    When I login successfully with "standard_user" and "secret_sauce"
    Then There are 6 product on the Inventory page


  Scenario: Redirect to Login page when unauthenticated user
    Given I am not a logged in user
    When I try to access the Inventory page
    Then I am redirected to Login page
    And I receive a Epic sadface error message


  Scenario: Add item to cart
    Given I am a logged in user
    And I am on the Inventory page
    When I add an item to cart
    Then The product button changes to Remove
    And The cart counter is incremented by one

  @single
  Scenario: Added item appear to Cart page
    Given I am a logged in user
    And I am on the Inventory page
    When I add an item to cart
    And I click on the cart button
    Then The item is on the Cart Page
    And Has the same description
    And Has the same price