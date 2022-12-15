*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page And Create Book

*** Test Cases ***
Search With Valid Acronym
    Go To References Page
    Set Search  tolkien
    Click Button  Search
    Page Should Contain  Title: Taru sormusten herrasta

Search With Valid Title
    Go To References Page
    Set Search  Taru sormusten herrasta
    Click Button  Search
    Page Should Contain  Title: Taru sormusten herrasta

Search With Valid Year
    Go To References Page
    Set Search  1954
    Click Button  Search
    Page Should Contain  Title: Taru sormusten herrasta

Search With Valid Author
    Go To References Page
    Set Search  J.R.R. Tolkien
    Click Button  Search
    Page Should Contain  Title: Taru sormusten herrasta

Search With Valid Publisher
    Go To References Page
    Set Search  WSOY
    Click Button  Search
    Page Should Contain  Title: Taru sormusten herrasta

Search With Valid Part Of Title
    Go To References Page
    Set Search  Taru
    Click Button  Search
    Page Should Contain  Title: Taru sormusten herrasta

*** Keywords ***
Set Acronym
    [Arguments]  ${acronym}
    Input Text  acronym  ${acronym}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Search
    [Arguments]  ${keyword}
    Input Text  keyword  ${keyword}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}


Go To Home Page And Create Book
    Go To Home Page
    Select Radio Button  radiobutton  book
    Click Button  Choose type
    Set Acronym  tolkien
    Set Title  Taru sormusten herrasta
    Set Author  J.R.R. Tolkien
    Set Year    1954
    Set Publisher  WSOY
    Click Button  Create book source
