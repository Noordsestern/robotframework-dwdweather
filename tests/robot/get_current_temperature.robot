*** Settings ***
Library    DwdWeatherLibrary
Force Tags    acceptance_test

*** Test Cases ***
Test 'Get current temperature from station' for address
    [Template]    Execute 'Get current temperature from station'
    Köln-Bonn
    33332 Gütersloh
    Aachen
    Berlin

*** Keywords ***
Execute 'Get current temperature from station'
    [Arguments]    ${address}
    ${current_temperature}    Get current temperature    ${address}
    Should Not Be Empty    ${current_temperature}    No temperature found for station:\t${address}