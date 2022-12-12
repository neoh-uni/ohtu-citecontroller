*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
See List
    Create Book
    Go To References Page
    Select Radio Button  radiobutton  all
    Click Button  Choose type
    Page Should Contain  Title: Taru sormusten herrasta

*** Keywords ***
Set Acronym
    [Arguments]  ${acronym}
    Input Text  acronym  ${acronym}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}


Create Book
    Select Radio Button  radiobutton  book
    Click Button  Choose type
    Set Acronym  tolkien
    Set Title  Taru sormusten herrasta
    Set Author  J. R. R. Tolkien
    Set Year    1954
    Set Publisher  WSOY
    Click Button  Create book source
