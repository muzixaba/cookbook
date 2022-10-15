'''
Doctest helps to run tests using docstrings.
You embed interactive python sessions and Doctest tests those.
Can be run by calling doctest.testmod() inside of script.
Also run at module-level `python -m doctest module_name.py -v`
'''

def adder(a, b):
    '''
    Returns the sum of a and b

    :param a: int
    :param b: int
    :return: int

    >>> adder(2, 3)
    5

    >>> adder("2", 2)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    >>> adder(2, "2")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    '''
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    result = a + b
    return(result)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# print(adder("2", 2))