<p align="center"><h1>Navigating the Automation Landscape with Selenium and Python🐍</h1></p>

This project contains an automated test suite written in Python using the **Pytest** framework and **Selenium** webdriver. The test suite was created as part of a learning exercise while studying automated testing with Selenium and Python. It tests the functionality of a sample e-commerce website, which serves as a template for a real-world e-commerce site. The goal of this project is to provide a foundation for understanding and utilizing automated testing with Selenium and Python.

The test suite is designed to cover the following core functionalities of the website:
- Navigation
- Visiting product page
- Adding item to the cart
- Testing login and registration features
- Testing user's cart

## Installation

1. Install Python 3.x from the official website.
2. Install Selenium using pip: `pip install selenium`
3. Install Chrome browser from the official website.
4. Clone this repository and navigate to the root directory.
5. Install the project dependencies using pip: `pip install -r requirements.txt`

## Running the tests

1. Open the terminal and navigate to the root directory of the cloned repository.
2. Run the tests using Pytest: `pytest -v --tb=line` or with custom language option using `pytest -v --tb=line --language=en`

The above command runs all test cases in the project. Please ensure that you have a stable internet connection while running the test suite as the tests interact with the live website to complete the testing.

## File Structure
- The project is structured using the Page Object Model pattern.
- The `conftest.py` file contains the browser setup and teardown methods
- The `pages` directory contains the page classes representing the various pages of the application
- The `test_*` files contain the test cases
- The `requirements.txt` contains the dependencies for this project
- `pytest.ini` is configuration file for pytest 

## Additional features:

- The test suite includes a `pytest` plugin that allows users to run the tests in different languages by using command line option `--language=es` for example.
- The `base_page.py` file contains common methods that are shared across all the page classes, like `is_element_present`, which is used to check the presence of an element on a page.
- The `locators.py` file contains the locators for all the elements used in the test suite.
- The `markers` feature in `pytest.ini` used to mark test cases and run specific groups of tests

## Debugging and Troubleshooting

- If the test fails due to element not being found, check if the locators are correct.
- If the browser is not working as expected, try updating the browser and webdriver versions.
- For more detailed logging and information during test execution, you can use the `-s` option when running the tests.

## Disclaimer

- All test cases were written according to the given assignments.
- The usage of the `parametrize` marker as it is, was carried out according to one of the assignments.
- The usage of markers for tests was carried out according to the assignments.
- The usage of the `assert` function was carried out according to the assignment. However, I would recommend using `raise - except` for exception handling in test cases.
- The function `solve_quiz_and_get_code` is used for the `alert` on the website to verify that the website is being accessed by a robot and not a human.
- The `setup` fixture was used exclusively for educational purposes. Manipulating the browser in the `setup` and even more so, checking something there is a bad practice. In real life, we would have implemented all these manipulations with the help of API or directly through the database.
- It is recommended to use the `logging` library for logging and debugging tests.

**Please keep in mind that any feature or functionality provided in this project is just a simulation, developed as a learning exercise.**

## My Observations

- Using fixtures in `setup` and `teardown` of test methods is a good way to control the environment of test and make sure it starts in a clean state for each test, but overuse of it should be avoided and setup should be done by API or directly through the database.
- Instead of using `Assert`, the better approach is using `raise - except` and exception handling to handle the test cases.
- `Logging` library is very helpful in debugging and reporting the test results.
- The `parametrize` marker is a good way to create multiple test cases with different input values but be sure it does not make test functions complex and hard to read.
- Always consider the performance and execution time of your test suites, try to avoid unnecessary waiting and use `Explicit Wait` instead of `Implicit Wait`.
- Use tags for grouping and running selective tests, it will save execution time and improve the testing process

## Resources and References

* [Selenium with Python documentation](https://selenium-python.readthedocs.io/)
* [Python Tutorials](https://docs.python.org/3/tutorial/)
* [Pytest documentation](https://docs.pytest.org/en/latest/)
* [WebDriver documentation](https://www.selenium.dev/documentation/webdriver/)
* [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest)

Please refer to these resources if you need additional information or guidance while working with this project.
