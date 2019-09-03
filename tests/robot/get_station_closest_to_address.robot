*** Settings ***
Library    DwdWeatherLibrary

*** Test Cases ***
Test title
    [Template]  Test 'Get station closest to address' with valid addesses
    Am Anger 33, 33332 Gütersloh    Nordrhein-Westfalen
    Harsewinkel    Nordrhein-Westfalen
    64807 Dieburg    Hessen
    Sundsvall   Västernorrland


*** Keywords ***
Test 'Get station closest to address' with valid addesses
    [Arguments]    ${address}   ${expected_state}
    ${station}    Get station closest to address    ${address}
    should not be empty  ${station}
    length should be  ${station}    8
    should be equal as strings  ${expected_state}    ${station}[state]