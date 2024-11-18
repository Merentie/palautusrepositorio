*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  jaakko123
    Set Password  12345678
    Set Password Confirmation  12345678
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  j
    Set Password  12345678
    Set Password Confirmation  12345678
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  bobias123
    Set Password  1234567
    Set Password Confirmation  1234567
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  bobias123
    Set Password  asdasdasd
    Set Password Confirmation  asdasdasd
    Submit Credentials
    Register Should Fail With Message  Password can't be constructed with letters only


Register With Nonmatching Password And Password Confirmation
    Set Username  bobias123
    Set Password  asdasdasd1
    Set Password Confirmation  asdasdasd2
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail with Message  User with username kalle already exists

Login After Successful Registration
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  j
    Set Password  12345678
    Set Password Confirmation  12345678
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long
    Go To Login Page
    Set Username  j
    Set Password  12345678
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}