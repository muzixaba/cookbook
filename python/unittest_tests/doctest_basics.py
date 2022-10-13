'''
Doctests helps to run tests using your docstrings.
You embed interactive python sessions and Doctest tests those.
Can be run by calling doctest.testmod() inside of script.
Also run at module-level `python -m doctest module_name.py -v`
'''

def adder(a, b):
    '''
    Returns the sum of a and b

    >>> adder(2, 3)
    5

    >>> adder(2, "2")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    '''
    result = a + b
    return(result)

if __name__ == "__main__":
    import doctest
    doctest.testmod()