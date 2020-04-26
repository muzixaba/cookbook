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

@pytest.mark.skip(reason="we don't do subtractions here")
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
        # checks if below code raises the expected error
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
    # Verify
    # assert if numbers are equal upto 2 decimal points
    assert_almost_equal(actual, desired, 2)