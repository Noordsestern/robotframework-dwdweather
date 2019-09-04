*** Settings ***
Library     DwdWeatherLibrary
Force Tags    acceptance_test

*** Test Cases ***
'Get station' should return a station for valid locations
    [Template]    'Get station' should return 1 station
    Aachen
    Bielefeld-Deppendorf
    Chemnitz
    Köln-Bonn
    München-Flughafen
    [Teardown]    Set Test Message    Completed getting stations.

'Get station' should return no station for fantasy locations
    [Template]    'Get station' should return no value
    Mordor
    Shire
    Neverland
    [Teardown]    Set Test Message    Completed getting no stations for fantasy locations.

*** Keywords ***
'Get station' should return 1 station
    [Arguments]    ${location}
    ${station}    Get station    ${location}
    Should Not Be Empty    ${station}    Could not retrieve station for ${location}
    Should Be Equal    ${location}    ${station}[name]    Failed to retrieve correct station

'Get station' should return no value
    [Arguments]    ${location}
    ${station}    Get station    ${location}
    Should Be Empty    ${station}    Could retrieve station for fantasy location:\t${location}\n
    
    
