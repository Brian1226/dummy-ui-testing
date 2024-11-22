# Shopping UI Test Automation
This project involves testing a [demo store](https://magento.softwaretestingboard.com/) in order to practice and develop skills in UI automation testing and following the Page Object Model (POM) design pattern. It tests both complete user journey (end-to-end tests) and some specific components of the website (component tests); the latter includes positive and negative tests. An HTML report is generated, which includes a summary of the test results.

## Technologies
- Python
- Selenium WebDriver
- pytest

## Prerequisites
- Have Python 3.x installed on your system

## Getting Started
1. Create a virtual environment
    ```
    python3 -m venv venv
    ```
2. Activate the virtual environment
    - On Windows
        ```
        venv\Scripts\activate
        ```
    - On Mac/Linux
        ```
        source venv/bin/activate
        ```
3. Clone the repository
    ```
    git clone https://github.com/Brian1226/shopping-ui-test-automation.git
    ```
4. Install the required dependencies
    ```
    pip3 install -r requirements.txt
    ```
5. Run the tests and generate an HTML report. Replace the value for the `browser` option with one of these: chrome, firefox, edge, or safari.  
    ```
    python3 -m pytest --browser=select_browser_here --html=reports/report.html --self-contained-html
    ```
