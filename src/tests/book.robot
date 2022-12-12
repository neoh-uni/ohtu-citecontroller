*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Adding Book With Valid Everything
    Select Radio Button  radiobutton  book
    Choose Type
    Set Acronym  tolkien
    Set Title  Taru sormusten herrasta
    Set Author  J.R.R. Tolkien
    Set Year    1954
    Set Publisher  WSOY
    Submit Reference
    Adding Should Succeed

#JOKU KENTTÄ TYHJÄ
Adding Book Without Year
    Select Radio Button  radiobutton  book
    Choose Type
    Set Acronym  tolkien
    Set Title  Taru sormusten herrasta
    Set Author  J.R.R. Tolkien
    Set Publisher  WSOY
    Submit Reference
    Adding Should Fail With Message  All fields must have a value

Adding Book Without Title
    Select Radio Button  radiobutton  book
    Choose Type
    Set Acronym  tolkien
    Set Author  J.R.R. Tolkien
    Set Year    1954
    Set Publisher  WSOY
    Submit Reference
    Adding Should Fail With Message  All fields must have a value

Adding Book Without Author
    Select Radio Button  radiobutton  book
    Choose Type
    Set Acronym  tolkien
    Set Title  Taru sormusten herrasta
    Set Year    1954
    Set Publisher  WSOY
    Submit Reference
    Adding Should Fail With Message  All fields must have a value

Adding Book Without Publisher
    Select Radio Button  radiobutton  book
    Choose Type
    Set Acronym  tolkien
    Set Title  Taru sormusten herrasta
    Set Author  J.R.R. Tolkien
    Set Year    1954
    Submit Reference
    Adding Should Fail With Message  All fields must have a value

Adding Book Without Acronym
    Select Radio Button  radiobutton  book
    Choose Type
    Set Title  Taru sormusten herrasta
    Set Author  J.R.R. Tolkien
    Set Year    1954
    Set Publisher  WSOY
    Submit Reference
    Adding Should Fail With Message  All fields must have a value

# JOKU KENTTÄ INVALID
Adding Book With Invalid Year
    Select Radio Button  radiobutton  book
    Choose Type
    Set Acronym  tolkien
    Set Title  Taru sormusten herrasta
    Set Author  J.R.R. Tolkien
    Set Year    2
    Set Publisher  WSOY
    Submit Reference
    Adding Should Fail With Message  Given year is not in range [500, 2027]

Adding Book With Invalid Author
    Select Radio Button  radiobutton  book
    Choose Type
    Set Acronym  tolkien
    Set Title  Taru sormusten herrasta
    Set Author  Author
    Set Year    1954
    Set Publisher  WSOY
    Submit Reference
    Adding Should Fail With Message  First name and surname is required
    

*** Keywords ***
Adding Should Succeed
    Page Should Contain  Book added

Adding Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

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


Submit Reference
    Click Button  Create book source

Choose Type
    Click Button  Choose type