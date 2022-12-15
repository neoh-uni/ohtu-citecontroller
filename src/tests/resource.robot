*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5
${HOME URL}  http://${SERVER}
${REFERENCES URL}  http://${SERVER}/references

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Go To Home Page
    Go To  ${HOME URL}

Go To References Page
    Go To  ${REFERENCES URL}
    