import pytest
from calculator import Calculator, CalculatorError


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

def test_division():
    """Test division"""
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(2, 0)