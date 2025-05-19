Feature: Importing vaccination records
  Scenario: Whitespace is normalised
    Given I am logged in as a nurse
    When I import vaccination records from mavis-vaccination-records-with-whitespace.csv
    Then I see the imported vaccination records
