
"""
>>> add(4,2)
6
>>> subtract(4,2)
2
>>> multiply(4,2)
8
"""

def add(x,y):
    """
    >>> add(7,6)
    13
    >>> add(-1,4)
    3
    """
    return x+y

def subtract(x,y):
    """
        >>> subtract(7,6)
        1
        >>> subtract(-1,4)
        -5
        """
    return x-y

def multiply(x,y):
    """
        >>> add(7,6)
        42
        >>> add(-1,4)
        -4
        """
    return x*y

add(5,6)

# terminal = python -m doctest doctest.py
# terminal = python -m doctest -v doctest.py
