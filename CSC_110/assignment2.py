BLOOD_ALCOHOL_LIMIT = 0.08
BLOOOD_ALCOHOL_WARNING = 0.05

def print_qualification_status(time_achieved: float, qualification_time: float):
    ''' This function should take the time achieved by racer and compare it the 
    time needed to qualify. If the achieved time is lower or equal 
    to the qualifying time, the function will print that you qualified 
    and print the difference between achieved time and the qualifying time. If 
    achieved time is higher than qualification time, it will print that you 
    missed qualification and tell you how much you missed it by
    
    Precondition: all times > 0
    
    >>> print_qualification_status(2.5,3)
    You qualified at 0.5 seconds below qualifying time
    
    >>> print_qualification_status(5.7, 3.8)
    You missed qualifying by 1.9 seconds
    
    >>> print_qualification_status(5.7, 5.7)
    You qualified at 0.0 seconds below qualifying time
    '''
    if time_achieved <= qualification_time:
        under_qualification = qualification_time - time_achieved
        
        print('You qualified at', round(under_qualification, 2), 
              'seconds below qualifying time')
        
    else:
        over_qualification = time_achieved - qualification_time
        
        print('You missed qualifying by', round(over_qualification,2), 
              'seconds')
        
        
def print_median(value1: float, value2: float, value3:float):
    ''' This function should take three numerical values and print the median 
    value
    >>> print_median(4, 4, 7)
    4
    >>> print_median(4, 7, 4)
    4
    >>> print_median(7, 4, 4)
    4
    >>> print_median(5, 5, 5)
    5
    >>> print_median(10, 9, 8)
    9
    >>> print_median(10, 8, 9)
    9
    >>> print_median(9, 10, 8)
    9
    >>> print_median(9, 8, 10)
    9
    >>> print_median(8, 10, 9)
    9
    >>> print_median(8, 9, 10)
    9
    >>> print_median(9.49, 10.43, 8.45)
    9.49
    >>> print_median(-76, -8, -10)
    -10
    '''
    #cases where value1 is the median
    if (value1 >= value2 and 
        value1 <= value3 or 
        value1 >= value3 and
        value1 <= value2):
        
        median = value1
        
    #cases where value2 is the median
    elif (value2 >= value1 and 
          value2 <= value3 or 
          value2 >= value3 and
          value2 <= value1):
        
        median = value2
    
    #all other cases can be covered with an else statement    
    else:
        median = value3
        
    print(median)
    
    
def print_triangle_type(side_a:float, side_b:float, side_c:float):
    ''' This function is designed to take the values of the three sides of a
    triangle and print whether if the triangle is isosceles, scalene or
    equilateral.
    
    Precondition: all values > 0
    
    >>> print_triangle_type(3.1,3.1,3.1)
    equilateral
    
    >>> print_triangle_type(4,2,4)
    isosceles
    
    >>> print_triangle_type(2,4,4)
    isosceles
    
    >>> print_triangle_type(4,4,2)
    isosceles
    
    >>> print_triangle_type(7,8,9)
    scalene
    
    >>> print_triangle_type(9,8,7)
    scalene
    
    >>> print_triangle_type(7,9,8)
    scalene
    
    >>> print_triangle_type(9,7,8)
    scalene
    
    >>> print_triangle_type(8,7,9)
    scalene
    
    >>> print_triangle_type(8,9,7)
    scalene
    '''
    
    if side_a == side_b and side_a == side_c:

        triangle_type = 'equilateral'
    
    elif (side_a == side_b or 
         side_b == side_c or 
         side_a == side_c):
        
        triangle_type = 'isosceles'
        
    else:
        triangle_type = 'scalene'
        
    print(triangle_type)
    
    
def is_multiple_of(n1: int, n2: int):
    ''' This function should print if n1 is a multiple of n2
    
    Precondition: type(n1) and type(n2) == int
    
    >>> is_multiple_of(5, 25)
    5 is not a multiple of 25
    
    >>> is_multiple_of(25, 5)
    25 is a multiple of 5
    
    >>> is_multiple_of(-8, -64)
    -8 is not a multiple of -64
    
    >>> is_multiple_of(-64, -8)
    -64 is a multiple of -8
    
    >>> is_multiple_of(73, 5)
    73 is not a multiple of 5
    '''
    if n1 % n2 == 0:
        print(n1, 'is a multiple of', n2)
    
    else:
        print(n1, 'is not a multiple of', n2)
        
        
def process_breathalizer_results(warnings: int, blood_alcohol: float):
    ''' This function is designed to take the number of past DUI warnings 
    someone has had, along with ther blood alcohol as a measure of mg/ml. 
    Anything at or above 0.08mg/ml is a fail. Anything less than 0.08mg/ml 
    but equal to or greater than 0.05 they may receive a warning.
    Under 0.05mg/ml is a pass.
    
    Along with printing 'PASS', 'FAIL' or 'Warning', the function will print any
    associated administrative penalties and the number of days prohibited from 
    driving
    
    >>> process_breathalizer_results(0, 0.03)
    PASS
    
    >>> process_breathalizer_results(1, 0.03)
    PASS
    
    >>> process_breathalizer_results(2, 0.03)
    PASS
    
    >>> process_breathalizer_results(0, 0.05)
    WARN
    ADMINISTRATIVE PENALTIES: $200
    IMMEDIATE DRIVING PROHIBITION LENTGH: 3 DAYS
    
    >>> process_breathalizer_results(1, 0.05)
    WARN
    ADMINISTRATIVE PENALTIES: $300
    IMMEDIATE DRIVING PROHIBITION LENTGH: 7 DAYS
    
    >>> process_breathalizer_results(2, 0.05)
    WARN
    ADMINISTRATIVE PENALTIES: $400
    IMMEDIATE DRIVING PROHIBITION LENTGH: 30 DAYS
    
    >>> process_breathalizer_results(0, 0.06)
    WARN
    ADMINISTRATIVE PENALTIES: $200
    IMMEDIATE DRIVING PROHIBITION LENTGH: 3 DAYS
    
    >>> process_breathalizer_results(1, 0.06)
    WARN
    ADMINISTRATIVE PENALTIES: $300
    IMMEDIATE DRIVING PROHIBITION LENTGH: 7 DAYS
    
    >>> process_breathalizer_results(2, 0.06)
    WARN
    ADMINISTRATIVE PENALTIES: $400
    IMMEDIATE DRIVING PROHIBITION LENTGH: 30 DAYS
    
    >>> process_breathalizer_results(0, 0.08)
    FAIL
    ADMINISTRATIVE PENALTIES: $500
    IMMEDIATE DRIVING PROHIBITION LENTGH: 90 DAYS
    
    >>> process_breathalizer_results(1, 0.08)
    FAIL
    ADMINISTRATIVE PENALTIES: $500
    IMMEDIATE DRIVING PROHIBITION LENTGH: 90 DAYS
    
    >>> process_breathalizer_results(2, 0.08)
    FAIL
    ADMINISTRATIVE PENALTIES: $500
    IMMEDIATE DRIVING PROHIBITION LENTGH: 90 DAYS
    
    >>> process_breathalizer_results(0, 0.09)
    FAIL
    ADMINISTRATIVE PENALTIES: $500
    IMMEDIATE DRIVING PROHIBITION LENTGH: 90 DAYS
    
    >>> process_breathalizer_results(1, 0.09)
    FAIL
    ADMINISTRATIVE PENALTIES: $500
    IMMEDIATE DRIVING PROHIBITION LENTGH: 90 DAYS
    
    >>> process_breathalizer_results(2, 0.09)
    FAIL
    ADMINISTRATIVE PENALTIES: $500
    IMMEDIATE DRIVING PROHIBITION LENTGH: 90 DAYS
    '''
    
    if blood_alcohol < BLOOOD_ALCOHOL_WARNING:
        print('PASS')
        
    elif blood_alcohol < BLOOD_ALCOHOL_LIMIT:
        print('WARN')
        
        if warnings < 1:
            print('ADMINISTRATIVE PENALTIES: $200')
            print('IMMEDIATE DRIVING PROHIBITION LENTGH: 3 DAYS')
            
        elif warnings == 1:
            print('ADMINISTRATIVE PENALTIES: $300')
            print('IMMEDIATE DRIVING PROHIBITION LENTGH: 7 DAYS')
            
        else:
            print('ADMINISTRATIVE PENALTIES: $400')
            print('IMMEDIATE DRIVING PROHIBITION LENTGH: 30 DAYS')        
    
    else:
        print('FAIL')
        print('ADMINISTRATIVE PENALTIES: $500')
        print('IMMEDIATE DRIVING PROHIBITION LENTGH: 90 DAYS')          
        

            

        