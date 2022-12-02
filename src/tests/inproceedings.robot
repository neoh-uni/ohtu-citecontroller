*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Adding Inproceedings With Valid Everything
    Set Title  inproceeding
    Set Author  Inproceedingin Kirjoittaja
    Set Year    2000
    Set Booktitle  booktitle
    Submit Reference
    Adding Should Succeed

#JOKU KENTTÄ TYHJÄ
Adding Inproceedings Without Year
    Select Radio Button  radiooptions  inproceedings
    Set Title  inproceeding
    Set Author  Inproceedingin Kirjoittaja
    Set Booktitle  booktitle
    Submit Reference
    Adding Should Fail With Message  Inproceedings must have a year

Adding Inproceedings Without Title
    Select Radio Button  radiooptions  inproceedings
    Set Author  Inproceedingin Kirjoittaja
    Set Year    2000
    Set Booktitle  booktitle
    Submit Reference
    Adding Should Fail With Message  Inproceedings must have a title

Adding Inproceedings Without Author
    Select Radio Button  radiooptions  inproceedings
    Set Title  inproceeding
    Set Year    2000
    Set Booktitle  booktitle
    Submit Reference
    Adding Should Fail With Message  Inproceedings must have an author

Adding Inproceedings Without Booktitle
    Select Radio Button  radiooptions  inproceedings
    Set Title  Inproceeding
    Set Author  Inproceedingin Kirjoittaja
    Set Year    2000
    Submit Reference
    Adding Should Fail With Message  Inproceedings must have a booktitle

# JOKU KENTTÄ INVALID
Adding Inproceedings With Invalid Year
    Select Radio Button  radiooptions  inproceedings
    Set Title  Inproceeding
    Set Author  Inproceedingin Kirjoittaja
    Set Year    2
    Set Booktitle  booktitle
    Submit Reference
    Adding Should Fail With Message  Given year is not in range 500, 2027

Adding Inproceedings With Invalid Title
    Select Radio Button  radiooptions  inproceedings
    Set Title  1
    Set Author  Inproceedingin Kirjoittaja
    Set Year    2000
    Set Booktitle  booktitle
    Submit Reference
    Adding Should Fail With Message  Given value is not a string.

Adding Inproceedings With Invalid Author
    Select Radio Button  radiooptions  inproceedings
    Set Title  Inproceeding
    Set Author  Author
    Set Year    2000
    Set Booktitle  booktitle
    Submit Reference
    Adding Should Fail With Message  First name and surname is required

Adding Inproceedings With Invalid Booktitle
    Select Radio Button  radiooptions  inproceedings
    Set Title  Inproceeding
    Set Author  Inproceedingin Kirjoittaja
    Set Year    2000
    Set Booktitle  2
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

Set Booktitle
    [Arguments]  ${Booktitle}
    Input Text  inputBooktitle  ${Booktitle}

Submit Reference
    Click Button  Create source
