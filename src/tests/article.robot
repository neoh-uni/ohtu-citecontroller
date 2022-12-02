*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
*** Test Cases ***
Adding Article With Valid Everything
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
    Set Title  Artikkeli
    Set Author  Artikkelin Kirjoittaja
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  Article must have a year

Adding Article Without Title
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  Article must have a Title

Adding Article Without Author
    Set Title  Artikkeli
    Set Year    2000
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  Article must have an author

Adding Article Without Journal
    Set Title  Artikkeli
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  Article must have a Journal

# JOKU KENTTÄ INVALID
Adding Article With Invalid Year
    Set Title  Artikkeli
    Set Author  Artikkelin Kirjoittaja
    Set Year    2
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  Given year is not in range 500, 2027

Adding Article With Invalid Title
    Set Title  1
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  Given value is not a string.

Adding Article With Invalid Author
    Set Title  Artikkeli
    Set Author  Author
    Set Year    2000
    Set Journal  Journal
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  First name and surname is required

Adding Article With Invalid Journal
    Set Title  Artikkeli
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Journal  3
    Set Volume  6
    Set Pages  20-22
    Submit Reference
    Adding Should Fail With Message  Given value is not a string.

Adding Article With Invalid Pages
    Set Title  Artikkeli
    Set Author  Artikkelin Kirjoittaja
    Set Year    2000
    Set Journal  Journal
    Set Volume  6
    Set Pages  abc
    Submit Reference
    Adding Should Fail With Message  message

Adding Article With Invalid Volume
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
    [Arguments]  ${Article_name}
    Input Text  Article_name  ${Article_name}

Set Author
    [Arguments]  ${author}
    Input Text  inputAuthorname  ${author}

Set Year
    [Arguments]  ${year}
    Input Text  inputYear  ${year}

Set Journal
    [Arguments]  ${journal}
    Input Text  inputJournal  ${journal}

Set Pages
    [Arguments]  ${pages}
    Input Text  inputJournal  ${pages}

Set Volume
    [Arguments]  ${volume}
    Input Text  inputJournal  ${volume}


Submit Reference
    Click Button  Create source