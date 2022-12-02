*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Adding Book With Valid Everything
    Set Title  kirja
    Set Author  Kirjan Kirjoittaja
    Set Year    2000
    Set Publisher  julkaisija
    Submit Reference
    Adding Should Succeed

#JOKU KENTTÄ TYHJÄ
Adding Book Without Year
    Set Title  kirja
    Set Author  Kirjan Kirjoittaja
    Set Publisher  julkaisija
    Submit Reference
    Adding Should Fail With Message  Book must have a year

Adding Book Without Title
    Set Author  Kirjan Kirjoittaja
    Set Year    2000
    Set Publisher  julkaisija
    Submit Reference
    Adding Should Fail With Message  Book must have a Title

Adding Book Without Author
    Set Title  kirja
    Set Year    2000
    Set Publisher  julkaisija
    Submit Reference
    Adding Should Fail With Message  Book must have an author

Adding Book Without Publisher
    Set Title  kirja
    Set Author  Kirjan Kirjoittaja
    Set Year    2000
    Submit Reference
    Adding Should Fail With Message  Book must have a publisher

# JOKU KENTTÄ INVALID
Adding Book With Invalid Year
    Set Title  kirja
    Set Author  Kirjan Kirjoittaja
    Set Year    2
    Set Publisher  julkaisija
    Submit Reference
    Adding Should Fail With Message  Given year is not in range 500, 2027

Adding Book With Invalid Title
    Set Title  4
    Set Author  Kirjan Kirjoittaja
    Set Year    2000
    Set Publisher  julkaisija
    Submit Reference
    Adding Should Fail With Message  Given value is not a string.

Adding Book With Invalid Author
    Set Title  kirja
    Set Author  Author
    Set Year    2000
    Set Publisher  julkaisija
    Submit Reference
    Adding Should Fail With Message  First name and surname is required

Adding Book With Invalid Publisher
    Set Title  kirja
    Set Author  Kirjan Kirjoittaja
    Set Year    2000
    Set Publisher  3
    Submit Reference
    Adding Should Fail With Message  Given value is not a string.

*** Keywords ***
Adding Should Succeed
    Page Should Contain  Reference added

Adding Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Set Title
    [Arguments]  ${book_name}
    Input Text  book_name  ${book_name}

Set Author
    [Arguments]  ${author}
    Input Text  inputAuthorname  ${author}

Set Year
    [Arguments]  ${year}
    Input Text  inputYear  ${year}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  inputPublisher  ${publisher}

Set Journal
    [Arguments]  ${journal}
    Input Text  inputPublisher  ${journal}

Set Booktitle
    [Arguments]  ${booktitle}
    Input Text  inputPublisher  ${booktitle}

Set Pages
    [Arguments]  ${pages}
    Input Text  inputPublisher  ${pages}

Set Volume
    [Arguments]  ${volume}
    Input Text  inputPublisher  ${volume}


Submit Reference
    Click Button  Create source
