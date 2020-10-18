# import pytest
import pytest

# Why tests fail
# AssertionError or another error happened before the assert statement

# Run pytest in IPython shell
!pytest test_module.py

# Test objects that contain/return floats
assert actual == pytest.approx(expected), message

# Testing for exceptions
with pytest.raises(ValueError):
    # If code inside context raises a ValueError, it will be silenced & test will Pass
    raise ValueError

with pytest.raises(ValueError):
    # If it doesn't, pytest raises Failed excpetion
    pass

with pytest.raises(ValueError) as err:
    raise ValueError("ValueError message")
# Assert that the message from the error is the same as the expected one
assert err.match("ValueError message")