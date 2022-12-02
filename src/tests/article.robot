*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
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
    Adding Should Fail With Message  Article must have a year

Adding Article Without Title
    Select Radio Button  radiobutton  article
    Choose Type
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  Article must have a Title

Adding Article Without Author
    Select Radio Button  radiobutton  article
    Choose Type
    Set Title  Artikkeli
    Set Year    2000
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  Article must have an author

Adding Article Without Journal
    Select Radio Button  radiobutton  article
    Choose Type
    Set Title  Artikkeli
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  Article must have a Journal

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
    Adding Should Fail With Message  Given year is not in range 500, 2027

Adding Article With Invalid Title
    Select Radio Button  radiobutton  article
    Choose Type
    Set Title  1
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  Given value is not a string.

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

Adding Article With Invalid Journal
    Select Radio Button  radiobutton  article
    Choose Type
    Set Title  Artikkeli
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Journal  3
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  Given value is not a string.

Adding Article With Invalid Pages
    Select Radio Button  radiobutton  article
    Choose Type
    Set Title  Artikkeli
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Journal  Journal
    Set Volume  6
    Set Pages  abc
    Submit Reference
    Adding Should Fail With Message  message

Adding Article With Invalid Volume
    Select Radio Button  radiobutton  article
    Choose Type
    Set Title  Artikkeli
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Journal  Journal
    Set Volume  abc
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  message

*** Keywords ***
Adding Should Succeed
    Page Should Contain  Reference added

Adding Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Set Title
    [Arguments]  ${article}
    Input Text  article  ${article}

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