import doctest


'''
Q1. Design a function that takes an integer n and prints 
print the squares of numbers from 0 to n separated by commas.
Your function should assume n is not negative.
'''

def squares_0_to_n(n: int) -> None:
    ''' This function should print the squares of 0 to a number inputed by the 
    user. Squares should be seperated by ',' and printed on the same line.
    
    Precondition n >= 0
    
    >>> squares_0_to_n(5)
    0,1,4,9,16,25
    
    >>> squares_0_to_n(0)
    0
    '''
    for i in range(n + 1):
        if i < n:
            print(i ** 2, end = ',')
        else:
            print(i ** 2)
        
        
    


'''
Q2. Design a function that takes an integer n and returns
the sum of the squares of numbers from 0 to n.
Your function should assume n is not negative.
'''
def get_sum_squares(n: int) -> int:
    ''' Return the sum of squares 0 to n inclusive
    
    Precondition n >= 0
    
    >>> get_sum_squares(0)
    0
    
    >>> get_sum_squares(5)
    55
    '''
    sum_of_squares = 0

    for i in range(n + 1):
        sum_of_squares += i ** 2
    
    return sum_of_squares


'''
Q3. Design a function that takes an integer n and prints 
prints the number n down to 1 followed by 'BLASTOFF!'
Your function should assume n is greater than 0.
'''
def print_launch(n: int) -> None:
    ''' This function will print a count down from n(inclusive) to 1 followed by
    'BLASTOFF!'
    
    Precondition: n > 0
    
    >>> print_launch(5)
    5 4 3 2 1 BLASTOFF!
    
    >>> print_launch(1)
    1 BLASTOFF!
    '''
    for i in range (n,0,-1):
        print(i, end = ' ')
        
    print('BLASTOFF!')

'''
Q4. Design a function that takes an integer n and a string and 
prints that string n times with no additional spaces or newlines.
Your function should assume n is not negative
You cannot use the * operator.
'''
def print_string_n_times(n: int, string: str) -> None:
    ''' This function should take an input and a string and print out that 
    string n times on the same line with no seperation
    
    preconditon: n > 0
    
    >>> print_string_n_times(0, 'abc')
    
    >>> print_string_n_times(4, 'abc')
    abcabcabcabc
    '''
    for i in range(n):
        print(string, end = '')


'''
Q5. Design a function that takes an integer n and a string and 
returns a new string that has the given string repeated n times
with no additional spaces or newlines.
Your function should assume n is not negative
You cannot use the * operator.
'''
def get_string_n_times(n: int, string: str) -> str:
    ''' This function should take an input and a string and print out that 
    string n times on the same line with no seperation
    
    preconditon: n > 0
    
    >>> print_string_n_times(0, 'abc')
    
    >>> print_string_n_times(4, 'abc')
    abcabcabcabc
    '''
    new_string = ''
    
    for i in range(n):
        new_string += string
        
    return new_string

