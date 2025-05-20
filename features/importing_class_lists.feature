Feature: Importing class lists
  Scenario: Whitespace is normalised
    Given a class list file named class-list.csv exists with:
      | nhs_number          | given_name | family_name  | year_group | address_line_1      |
      |  899	535 1918 | Hari       | Sel‍don    | 8          | 1\n  Helicon\n  Way |
    And I am logged in as a nurse

    When I import a class list from class-list.csv for 'Al-Hira School'
    Then I see a completed import
    And I see the following child details:
      | NHS number | 899 535 1918  |
      | Full name  | SELDON, Hari  |
      | Address    | 1 Helicon Way |
