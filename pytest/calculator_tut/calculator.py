import numbers

class CalculatorError(Exception):
    """Exception class for calculator"""

class Calculator:
    """Class to create Calculator instances"""

    def add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        try:
            res = a + b
            return res
        except TypeError:
            raise CalculatorError()

    def minus(self, a, b):
        res = a - b
        return res

    def divide(self, a, b):
        try:
            res = a / b
        except ZeroDivisionError:
            raise CalculatorError("Can't divide by zero")
        return res

    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f"'{operand}' is not a number")