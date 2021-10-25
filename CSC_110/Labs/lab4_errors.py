import doctest
"""
INSTRUCTIONS:
The following functions have errors in them.  Find and fix the errors.  
We encourage you to experiment with the debugger.

Save and submit your fixed version of this file with 
the filenname, function names and the function arguments unchanged.
"""

def sum(n:int) -> int:
    """ computes the sum of the numbers 1 to n inclusive and returns it
    Precondition: n>0
    >>> sum(1)
    1
    >>> sum(10)
    55
    """
    sum = 0
    
    for num in range(1,n+1):
        sum += num
        
    return sum


def product(n:int) -> int:
    """ computes the product of the numbers 1 to n inclusive and returns it
    Precondition: n>0
    >>> product(1)
    1
    >>> product(10)
    3628800
    """
    product = 1
    
    for num in range(1, n + 1):
        product *= num
        
    return product