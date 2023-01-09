Feature: SWAGLABS Login Page

  Scenario Outline: Login fail
    Given I am on the Sign in page
    When I input a "<username>" username
    And I input a "<password>" password
    And I click the login button
    Then I receive the Epic sadface error message
    Examples: Credentials
      | username      | password     |
      | fake_user     | fake_pass    |
      | standard_user | fake_pass    |
      | fake_user     | secret_sauce |

