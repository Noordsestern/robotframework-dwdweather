*** Settings ***
Library     DwdWeatherLibrary
Force Tags    acceptance_test

*** Test Cases ***
'Get all stations' should return staitons
    ${stations}    When Get all stations
    Then Should Not Be Empty    ${stations}    No stations could be retrieved from DWD
    And Log    ${stations}
    ${amount_of_stations}   And Get Length    ${stations}
    And Set Test Message     Found ${amount_of_stations} stations