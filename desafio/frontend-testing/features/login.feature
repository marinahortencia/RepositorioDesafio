#Behave

Feature: Login
    
    Background: Setup
        Given I enter on main url
        When  I am on home screen
        And   I click on sign
        


    Scenario: TC_001 - Verify that it is possible login
        Given I am on login screen
        And   I type the email "marina.teste@gmail.com"
        And   I type the password "123456"
        And   I click on login button
							
						