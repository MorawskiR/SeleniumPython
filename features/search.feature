Feature: Search in helion.pl
Scenario: Fill search input in webpage
  Given user open helion.pl
  When user fills "python" search input
  Then Search result = python