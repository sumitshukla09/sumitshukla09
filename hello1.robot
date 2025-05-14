*** Settings ***
Documentation     Complete test suite for login, logout, and a basic post-login action
Library           SeleniumLibrary

*** Variables ***
${LOGIN_URL}          https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${USERNAME}           Admin
${PASSWORD}           admin123
${BROWSER}            Chrome

${USERNAME_FIELD}     name=username
${PASSWORD_FIELD}     name=password
${LOGIN_BUTTON}       xpath=//button[@type='submit']
${DASHBOARD_ELEMENT}  xpath=//h6[text()='Dashboard']
${LOGOUT_MENU}        xpath=//span[@class='oxd-userdropdown-tab']
${LOGOUT_LINK}        xpath=//a[text()='Logout']
${MENU_LINK}          xpath=//span[text()='PIM']
${MENU_PAGE_HEADER}   xpath=//h6[text()='PIM']

*** Test Cases ***
Valid Login And Logout
    [Documentation]    User should be able to login and logout successfully
    Open Browser To Login Page
    Input Credentials
    Submit Login
    Verify Dashboard Page
    Logout
    Verify Login Page

Perform Action After Login
    [Documentation]    Perform a basic action after login
    Open Browser To Login Page
    Input Credentials
    Submit Login
    Click Some Menu
    Verify Page Header    PIM
    Logout
    Verify Login Page

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    ${USERNAME_FIELD}    10s

Input Credentials
    Input Text    ${USERNAME_FIELD}    ${USERNAME}
    Input Text    ${PASSWORD_FIELD}    ${PASSWORD}

Submit Login
    Click Button    ${LOGIN_BUTTON}
    Wait Until Element Is Visible    ${DASHBOARD_ELEMENT}    10s

Verify Dashboard Page
    Element Should Be Visible    ${DASHBOARD_ELEMENT}

Click Some Menu
    Click Element    ${MENU_LINK}
    Wait Until Element Is Visible    ${MENU_PAGE_HEADER}    10s

Verify Page Header
    [Arguments]    ${expected_text}
    Element Text Should Be    ${MENU_PAGE_HEADER}    ${expected_text}

Logout
    Click Element    ${LOGOUT_MENU}
    Wait Until Element Is Visible    ${LOGOUT_LINK}    5s
    Click Element    ${LOGOUT_LINK}
    Wait Until Element Is Visible    ${USERNAME_FIELD}    10s

Verify Login Page
    Element Should Be Visible    ${USERNAME_FIELD}

*** Suite Teardown ***
Close Browser
