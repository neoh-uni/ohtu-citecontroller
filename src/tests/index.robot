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
    [Arguments]  ${year}
    Input Text  inputPublisher  ${publisher}



Submit Reference
    Click Button  Create source
