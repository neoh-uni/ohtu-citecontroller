*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${SERVER}  citecontroller.herokuapp.com/
${BROWSER}  headlesschrome
${DELAY}  0
${HOME URL}  http://${SERVER}

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Go To Home Page
    Go To  ${HOME URL}