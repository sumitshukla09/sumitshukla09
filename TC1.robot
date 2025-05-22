*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}  chrome
${NEW_USER} VVivek
${USER_ROLE} Admin
${USER_STATUS} Enabled
${USER_PASSWORD} Vivek123

*** Test Cases ***
Login
    Open Browser        ${url}      ${browser}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://input[@name="username"]    10 seconds
    Input Text          xpath://input[@name="username"]     Admin
    Input Text          xpath://input[@name="password"]     admin123
    Click Button        xpath://button[@type="submit"]
    Wait Until Page Contains    Dashboard    10 seconds
    Close Browser

# Add remaining test cases below Login...
