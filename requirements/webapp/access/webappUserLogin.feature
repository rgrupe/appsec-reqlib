Feature: Webapp User Login

Description: As a User, I want to log into a webapp, so that I can access the provided functionality.

Scenario: Compliant Login

    Given: I am a webapp registered user with an active account.
    When: I enter my account as user1.
        And: I enter my password as Secret#1
    Then: I am logged in successfully.
        And: I can view the successful login page.
    Examples:
    | Role | Account | Password |
    | Member_Primary  | Value 2  | Value 3  |
    | Member_Dependent  | Value 2  | Value 3  |
    | Group_Admin  | Value 2  | Value 3  |
    | App_Admin  | Value 2  | Value 3  |

Scenario: Missing Account

Scenario: Missing Password

Scenario: Incorrect Account

Scenario: Incorrect Password

Scenario: Incorrect Account too many attempts (>5)

Scenario: Incorrect Password too many atempts