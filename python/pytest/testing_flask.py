""""
#-----------------
# Folder Structure
#-----------------
- venv
- app.py
- project
    - __init__.py
    - models
    - views
- tests
    - unit
        - __init__.py
        - test_models.py
    - integration
        - __init__.py
        - test_views.py
        - test_urls.py
- requirements.txt
- .gitignore
"""

# All test files and test functions must be in a folder called 'tests_* or test_*'

"""
#------------------------
# Document test functions
#------------------------

def test_function_name():
    '''
    GIVEN - initial condition for test
    WHEN - test is run
    THEN - assert expected result
    '''
"""




# running pytest
# run through python interpreter
python -m pytest

# run in verbose mode
python -m pytest -v

# run in verbose mode and run last failed tests
python -m pytest -v --last-failed

# run specific types of tests
python -m pytest tests/unit

# run specific types of tests, showing setup/tear-down from fixtures
python -m pytest --setup-show tests/unit


#-----------------
# FIXTURES 
#-----------------
# Fixtures initialise tests to a known state
    # Fixtures are functions that are run before and after each test
# Defined as functions in tests/conftest.py
# Fixture Scope
# - function: run once per test function (default)
# - module: run once per module (per test file)
# - class: run once per class
# - package: run once per package
# - session: run once per session (per call to pytest)

#-------------------
# Code Coverage
#--------------------
# Code coverage is a metric of how much source code is tested
# Python packages for code coverage:
# - coverage.py
# - pytest-cov

# Check code coverage in pytest
python -m pytest --cov=project
