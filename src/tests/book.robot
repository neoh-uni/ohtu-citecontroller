*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Adding Book With Valid Everything
    Select Radio Button  radiobutton  book
    Choose Type
    Set Title  kirja
    Set Author  Kirjan Kirjoittaja
    Set Year    2000
    Set Publisher  julkaisija
    Submit Reference
    Adding Should Succeed

#JOKU KENTTÄ TYHJÄ
Adding Book Without Year
    Select Radio Button  radiobutton  book
    Choose Type
    Set Title  kirja
    Set Author  Kirjan Kirjoittaja
    Set Publisher  julkaisija
    Submit Reference
    Adding Should Fail With Message  All fields must have a value

Adding Book Without Title
    Select Radio Button  radiobutton  book
    Choose Type
    Set Author  Kirjan Kirjoittaja
    Set Year    2000
    Set Publisher  julkaisija
    Submit Reference
    Adding Should Fail With Message  All fields must have a value

Adding Book Without Author
    Select Radio Button  radiobutton  book
    Choose Type
    Set Title  kirja
    Set Year    2000
    Set Publisher  julkaisija
    Submit Reference
    Adding Should Fail With Message  All fields must have a value

Adding Book Without Publisher
    Select Radio Button  radiobutton  book
    Choose Type
    Set Title  kirja
    Set Author  Kirjan Kirjoittaja
    Set Year    2000
    Submit Reference
    Adding Should Fail With Message  All fields must have a value

# JOKU KENTTÄ INVALID
Adding Book With Invalid Year
    Select Radio Button  radiobutton  book
    Choose Type
    Set Title  kirja
    Set Author  Kirjan Kirjoittaja
    Set Year    2
    Set Publisher  julkaisija
    Submit Reference
    Adding Should Fail With Message  Given year is not in range [500, 2027]

Adding Book With Invalid Author
    Select Radio Button  radiobutton  book
    Choose Type
    Set Title  kirja
    Set Author  Author
    Set Year    2000
    Set Publisher  julkaisija
    Submit Reference
    Adding Should Fail With Message  First name and surname is required
    

*** Keywords ***
Adding Should Succeed
    Page Should Contain  Book added

Adding Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

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


Submit Reference
    Click Button  Create source

Choose Type
    Click Button  choose type