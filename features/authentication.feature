Feature: Authentication
  Scenario Outline: Logging in and out (<role>)
    Given I am logged in as a <role>
    Then I see the following dashboard links:
      | Programmes                  |
      | Sessions                    |
      | Children                    |
      | Unmatched consent responses |
      | School moves                |
      | Import records              |
      | Vaccines                    |
      | Your organisation           |
      | Service guidance            |
    When I log out
    Then I see the start page

    Examples:
      | role  |
      | admin |
      | nurse |
      | superuser |

  Scenario Outline: Invalid username or password ('<username>' and '<password>')
    Given I am on the log in page
    When I try to log in with '<username>' and '<password>'
    Then I see the message 'Invalid Email or password.'

    Examples:
      | username | password |
      |          |          |
      | invalid  |          |
      |          | invalid  |
      | invalid  | invalid  |
