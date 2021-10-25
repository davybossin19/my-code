import doctest

def compute_harmonic_series(n: int) -> float:
    ''' This function should the an integer n and return the harmonic series to 
    n. Example 1 + 1/2 + 1/3 + 1/4 ... 1/n
    
    preconditon: n >= 0
    
    >>> compute_harmonic_series(0)
    0
    
    >>> compute_harmonic_series(1)
    1.0
    
    >>> compute_harmonic_series(3)
    1.8333333333333333
    
    >>> compute_harmonic_series(5)
    2.283333333333333
    '''
    if n == 0:
        return 0
    
    else: 
        h_series = 0
        
        for i in range(1, n + 1):
            h_series += 1/i
            
        return h_series
    

def get_fibonacci_sequence(n: int) -> str:
    ''' This function will return a string with the first n values of the 
    fibbonaci sequence in a string with values seperated by commas
    
    precondition: n >= 0
    
    >>> get_fibonacci_sequence(0)
    ''
    
    >>> get_fibonacci_sequence(1)
    '0'
    
    >>> get_fibonacci_sequence(2)
    '0,1'
    
    >>> get_fibonacci_sequence(3)
    '0,1,1'
    
    >>> get_fibonacci_sequence(4)
    '0,1,1,2'
    
    >>> get_fibonacci_sequence(9) 
    '0,1,1,2,3,5,8,13,21'
    '''
    if n == 0:
        return ''
    
    elif n == 1:
        return '0'
    
    elif n == 2:
        return '0,1'    
    
    else:
        fib_sequence_to_n = '0,1,'
        x = 0
        y = 1
        
        for i in range(n - 3):
            z = x + y
            fib_sequence_to_n += str(z) + ','
            x = y
            y = z
            
        fib_sequence_to_n += str(x + y)
        
        return fib_sequence_to_n
    
    
def print_pattern(height: int, width: int, str1: str, str2: str) -> None:
    ''' This function will take two ints and two strings and print a pattern 
    with a height and width specified by your ints and lines of alternating 
    combination of your string inputs
    
    precondition: height > 0 and width > 0
    
    >>> print_pattern(4,3,'!@','$$$')
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    
    >>> print_pattern(1,1,'3','4')
    34
    
    >>> print_pattern(3,1,'3','4')
    34
    43
    34
    
    >>> print_pattern(3,2,'3','4')
    3434
    4343
    3434
    
    >>> print_pattern(3,1,'3','')
    3
    3
    3
    
    >>> print_pattern(1,1,'3','')
    3
    
    >>> print_pattern(3,1,'3','')
    3
    3
    3
    
    >>> print_pattern(3,1,'','f')
    f
    f
    f
    
    >>> print_pattern(3,3,'3','')
    333
    333
    333
    
    >>> print_pattern(3,3,'','f')
    fff
    fff
    fff
    
    >>> print_pattern(3,3,'','')
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    '''
    
    comb_str1 = str1 + str2
    comb_str2 = str2 + str1
    
    pattern_line = comb_str1 * width
    alt_pattern_line = comb_str2 * width
    
    for i in range(1, height + 1):
        if i % 2 == 1: 
            print(pattern_line)
        else:
            print(alt_pattern_line)
    
    