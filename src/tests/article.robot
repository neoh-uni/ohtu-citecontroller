*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Adding Article With Valid Everything
    Select Radio Button  radiobutton  article
    Choose Type
    Set Title  Artikkeli
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Succeed

#JOKU KENTTÄ TYHJÄ
Adding Article Without Year
    Select Radio Button  radiobutton  article
    Choose Type
    Set Title  Artikkeli
    Set Author  Artikkelin Kirjoittaja
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  All fields must have a value

Adding Article Without Title
    Select Radio Button  radiobutton  article
    Choose Type
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  All fields must have a value

Adding Article Without Author
    Select Radio Button  radiobutton  article
    Choose Type
    Set Title  Artikkeli
    Set Year    2000
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  All fields must have a value

Adding Article Without Journal
    Select Radio Button  radiobutton  article
    Choose Type
    Set Title  Artikkeli
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  All fields must have a value

# JOKU KENTTÄ INVALID
Adding Article With Invalid Year
    Select Radio Button  radiobutton  article
    Choose Type
    Set Title  Artikkeli
    Set Author  Artikkelin Kirjoittaja
    Set Year    2
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  Given year is not in range [500, 2027]

Adding Article With Invalid Author
    Select Radio Button  radiobutton  article
    Choose Type
    Set Title  Artikkeli
    Set Author  Author
    Set Year    2000
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  First name and surname is required


*** Keywords ***
Adding Should Succeed
    Page Should Contain  Article added

Adding Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Set Title
    [Arguments]  ${article}
    Input Text  title  ${article}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Pages
    [Arguments]  ${pages}
    Input Text  pages  ${pages}

Set Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}


Submit Reference
    Click Button  Create source

Choose Type
    Click Button  choose type