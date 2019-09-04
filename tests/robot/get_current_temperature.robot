*** Settings ***
Library    DwdWeatherLibrary
Force Tags    acceptance_test

*** Test Cases ***
Test 'Get current temperature from station' for address
    [Template]    Execute 'Get current temperature from station'
    33332 Gütersloh
    Aachen
    Berlin

*** Keywords ***
Execute 'Get current temperature from station'
    [Arguments]    ${address}
    ${station}    Get station closest to address    ${address}
    should not be empty    ${station}    No station found for address:\t${address}
    ${current_temperature}    Get current temperature    ${station}
    Should Not Be Empty    ${current_temperature}    No temperature found for station:\t${station}[name]