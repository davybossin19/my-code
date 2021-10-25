import doctest

ADULT = 18
SENIOR = 65
CHILD_RATE = 1.50
ADULT_RATE = 2.50
SENIOR_RATE = 2.00
GROUP_DISCOUNT = 0.10

''' 
Q1. Design a function that will take two numbers and 
returns the sum of those numbers
'''

def add(num1: float, num2: float) -> float:
    ''' returns the sum of n1 and num2
    >>> add(4, 5)
    9
    >>> add(2.2, 3.6)
    5.8
    '''
    
    sum_of_nums = num1 + num2
    
    return sum_of_nums



'''
Q2. Below is the print_fare function we wrote in a past lecture.

Continuing in this problem domain, design a separate function that takes
the number of children, number of adults and number of seniors 
and returns the total fare for those riders.  You function should take into
acount a group discount of 10% for groups of 10 or more.

You can assume the function will not be passed negative values.
'''

def print_fare(age:int):
    '''
    determines the bus fare for a rider of the given age and prints it
    
    Precondition: age > 0
    >>> print_fare(1)
    The fare is: $ 1.50
    >>> print_fare(17)
    The fare is: $ 1.50
    >>> print_fare(18)
    The fare is: $ 2.50
    >>> print_fare(64)
    The fare is: $ 2.50
    >>> print_fare(65)
    The fare is: $ 2.00
    '''
    if age < ADULT:
        fare = CHILD_RATE
    elif age < SENIOR:
        fare = ADULT_RATE
    else:
        fare = SENIOR_RATE
       
    print('The fare is: $', format(fare, '0.2f'))
    
def total_fare(children: int, adults: int, seniors: int) -> float:
    '''This function should take how many children, adults and seniors riding
    the bus and return the total fare of all those riders. Function applies a 
    10% discount for groups of 10 or more
    
    precondition: all categories of riders must be > 0
    
    >>> total_fare(5, 5, 5)
    27.0
    '''
    fare = (children * CHILD_RATE + 
            adults * ADULT_RATE + 
            seniors * SENIOR_RATE)
    
    riders = children + adults + seniors
    
    if riders >= 10:
        fare -= fare * GROUP_DISCOUNT
        
    return fare
        
'''
Q3. Design a function that takes two strings and returns the
result of those two strings joined together.
'''
def concatenate(str1: str, str2: str) -> str:
    ''' This function concatenates two strings
    >>> concatenate('','')
    ''
    >>> concatenate('abc','def')
    'abcdef'
    '''
    joined_string = str1 + str2
    
    return joined_string


'''
Q4. Recall we designed the following function in a past lecture.
Update this function so it does not print the roman numeral, 
but instead returns it.
'''
def print_roman_numeral(num:int):
    '''
    determines and prints the corresponding roman numeral for the given num
    
    Precondition: 1 <= num <=10
    
    >>> print_roman_numeral(1)
    I
    >>> print_roman_numeral(2)
    II
    >>> print_roman_numeral(3)
    III
    >>> print_roman_numeral(4)
    IV
    >>> print_roman_numeral(5)
    V
    >>> print_roman_numeral(6)
    VI
    >>> print_roman_numeral(7)
    VII
    >>> print_roman_numeral(8)
    VIII
    >>> print_roman_numeral(9)
    IX
    >>> print_roman_numeral(10)
    X
    '''
    
    if num==1:
        print('I')
    elif num==2:
        print('II')
    elif num==3:
        print('III')
    elif num==4:
        print('IV')    
    elif num==5:
        print('V')
    elif num==6:
        print('VI')
    elif num==7:
        print('VII')  
    elif num==8:
        print('VIII')
    elif num==9:
        print('IX')
    else:
        print('X')  

'''
Q5. Design a function that takes the amount of time an
object takes to fall after being dropped in seconds.
The function calculates and returns the distance the object fell in meters,
where the formula for distance is:
        d = 1/2 gt^2
        where t is the time in seconds and
        g is gravitational acceleration is constant at 9.8 m/s^2
        d is in meters
If the function is passed a negative value for time it should 
return the value -1 to indicate an error.
'''