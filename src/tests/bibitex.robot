*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
See List Of Just Bibitex
    Create Book
    Go To References Page
    Select Radio Button  radiobutton  bibitex
    Click Button  choose type
    Page Should Contain  author = {Kirjan Kirjoittaja},

*** Keywords ***
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
    Click Button  choose type
    Set Title  kirja
    Set Author  Kirjan Kirjoittaja
    Set Year    2000
    Set Publisher  julkaisija
    Click Button  Create source