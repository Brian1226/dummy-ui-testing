# Test Plan for Shopping UI Test Automation
Prepared by: Brian Nguyen
<br>
Date: May 2024

## Objective
This test plan outlines the strategy for performing UI automation testing on the demo store’s registration and login process, product selection, cart functionality, and checkout workflow. The testing will ensure that the store’s key features function correctly from end to end. Automated tests will be developed using Python, Selenium WebDriver, and pytest, following the Page Object Model (POM) design pattern.

## Scope
- In scope: registration, login, buying products, adding to the shopping cart, selecting shipping and payment methods, and confirmation that the purchase has been successful
- Out of scope: adding products to the wishlist, writing reviews for products, and removing products from the shopping cart

## Test Strategy
- End-to-End testing: verify the complete user journey from registration to checkout
- Functional testing: verify each feature with positive and negative scenarios
- Cross-browser testing: ensure compatibility across different browsers

## Test Criteria
- All test cases must pass
- Test coverage of at least 90% for identified scenarios

## Test Deliverables
- Test cases
- Automated test scripts
- HTML test report with a summary of test results

## Test Schedule
- Planning and creating test cases: 1 day
- Developing automated test scripts: 1 week
- Executing tests to ensure all test cases pass, reporting: 2 days

# Test Tools & Environment
- Tools & Technologies: Python, Selenium WebDriver, pytest, Git, Github
- Operating System: macOS
- Browsers: Chrome, Safari, Edge, Firefox

# Risks
- Test script may break due to UI changes (element locators, page structure)
- Test script may break due to dynamic content not handled correctly
- Server downtime
- Pages load slow, so tests may fail due to timeouts
- Test data is missing or incorrect
- Test coverage gaps
- Browser compatibility issues
