import pytest
from calculator import Calculator, CalculatorError
from numpy.testing import assert_almost_equal

def test_add():
    """Test add function"""
    calc = Calculator()
    the_sum = calc.add(2,3)
    assert the_sum == 5

def test_add_type_mix():
    """Test if operands are different types"""
    calc =  Calculator()
    # with pytest.raises(CalculatorError):
    return calc.add("one", 2)

def test_add_strings():
    """Testing if strings can be added"""
    calc = Calculator()
    return calc.add("one", "two")

# @pytest.mark.skip(reason="we don't do subtractions here")
def test_minus():
    """Test subtraction"""
    calc = Calculator()
    diff = calc.minus(5,1)
    assert diff == 4


# Use parametrize to test multiple values
@pytest.mark.parametrize(
    'a, b, expected', [
        (8, 2, 4),
        (10, 5, 2),
        (100, 2, 50)
    ]
)
def test_division(a,b, expected):
    """Test division"""
    calc = Calculator()
    assert calc.divide(a, b) == expected

def test_zero_division():
    """Test for ZeroDivisionError"""
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        # If below code raises the expected error, the test passes
        calc.divide(2, 0)

# Can group tests using classes
# class TestAdd:

# Use Fixtures for setup & code reuse

# Steps in test function:
    # Setup
    # Exercise
    # Verify
    # Cleanup
def test_floating_point_numbers():
    # setup
    desired = 0.293
    # Exercise 
    actual = 1 - 0.707
    # Verify (run the specific function to see what get what it actually returns)
    # assert if numbers are equal upto 2 decimal points
    assert_almost_equal(actual, desired, 2)


#==============
# Mocking
#==============
# It's the process of fooling a test into thinking something
# was ran in production.
# Runs testing function independently of their dependancies
# Requires that a mocking function be created
# @patch decorator is used to replace production function with mock version
# from unittest.mock import patch
#  @patch('package.module.func_name', new=mock_func_name)
# Mock functions where they are use & not where they are defined
# Can also use the mock function as a context manager
# Can also use mock inline by using setUp() and tearDown()

#==============
# Fixtures
#==============
# Creates a source of data that's used multiple times e.g. Setup function/data
# fixture functions have @pytest.fixture decorator & are outside the tests
# tmpdir is a built-in fixture for the creation & teardown of temp directories


#==============
# Coverage Report
#================
# pip install pytest-cov
# pytest --cov (returns summary coverage report)
# pytest --cov-report term-missing --cov (return coverage with missing lines)


#=========================
# How many tests per unit
#=========================
# 2-5 for Normal Arguments(happy path)
# Test for bad arguments
# Test for Boundary Values
# Test for Special Logic


#===================
# Test Classes
#===================
# Help to organise tests for specific functions/units
# class TestFunctionName:
# All tests for function_name become methods under TestFunctionName class


#=================================
# When you expect a test to fail
#=================================
@pytest.mark.xfail(reason="My reason for why the test fails")
def test_func_name():
    pass

#========================================
# Skip test if certain condition is True
#========================================
@pytest.mark.skipif(condition, reason="My reason for skipping.")
def test_func_name():
    pass