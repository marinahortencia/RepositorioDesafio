#Behave

Feature: Search
    
    Background: Setup
        Given I enter on main url
        When  I am on home screen
        And   I type the search text "Faded Short Sleeve"
        And   I click on search button
        


    Scenario: TC_001 - Verify that it is possible to search
        Given I am on search screen
        Then  I verify that result number is correct "1 result has been found."
        And   I verify that product name is equal to searched "Faded Short Sleeve T-shirts"
        When  I click on product details
        Then  I verify the product condition is equal to displayed "New"
        And   I verify that the product description is "Faded short sleeve t-shirt with high neckline. Soft and stretchy material for a comfortable fit. Accessorize with a straw hat and you're ready for summer!"
							
						