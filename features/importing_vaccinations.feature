Feature: Importing vaccination records
  Scenario: Whitespace is normalised
    Given a Mavis vaccinations file named vaccinations.csv exists with:
      | nhs_number          | given_name | family_name  | year_group |
      |  860	706 9403 | Ha\nri     | Sel‍don    | 8          |
    And I am logged in as a nurse

    When I import vaccinations from vaccinations.csv
    Then I see a completed import
    And I see the following vaccination details:
      | NHS number | 860 706 9403  |
      | Full name  | SELDON, Hari  |
