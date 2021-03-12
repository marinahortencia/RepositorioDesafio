#Behave

Feature: Purchase
    
    Background: Setup
        Given I enter on main url
        When  I am on home screen
        And   I click on sign
        Given I am on login screen
        And   I type the email "marina.teste@gmail.com"
        And   I type the password "123456"
        And   I click on login button
        When  I am on home screen
        And   I type the search text "Faded Short Sleeve"
        And   I click on search button
        Given I am on search screen 
        And   I click on product details

    Scenario: TC_001 - Verify that it is possible to buy a product
        Given I am on Purchase screen
        And   I click on add to cart button
        Then  I verify the the product is added "Product successfully added to your shopping cart"
        When  I click on proceed checkout cart button
        And   I click on proceed checkout sumary button
        And   I click on proceed checkout address button
        Then  I verify the term message to agree "I agree to the terms of service and will adhere to them unconditionally."
        When  I click on agree checkbox
        And   I click on proceed checkout shipping button
        And   I click on payment check option
        And   I click confirm order

        
							
						