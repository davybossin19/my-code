import doctest

ADULT = 18
SENIOR = 65

CHILD_RATE = 1.5
ADULT_RATE = 2.5
SENIOR_RATE = 2.0

NUM_BUNS_PER_PACK = 8
NUM_DOGS_PER_PACK = 12

'''
Q1. You were asked to design a function that determines the cost of 
riding the bus based on the value of the argument age of type int.  
If age is less than 18, the cost is $1.50.  
If age is 65 or more, the cost is $2.00.  
For all other values of age, the cost is $2.50.   

A friend of yours submitted the following code but was deducted marks for: 
-inappropriate use of branching constructs
-redundant Boolean expressions
-magic numbers
-insufficient test coverage
-missing units in output

Edit the function in light of the feedback from the marker.
'''
def get_fare(age: int):
    '''
    determines the bus fare for a rider of the given age and prints it
    
    Precondition: age > 0
    
    >>> get_fare(15)
    The fare is: 1.50
    '''
    if age < ADULT :
        fare = CHILD_RATE
    elif age >= SENIOR :
        fare = SENIOR_RATE
    else:
        fare = ADULT_RATE
       
    print('The fare is:', format(fare, '.2f'))



'''
Q2. The following function design passes all of the given 
example tests but there are still problems with it.
Find and fix the problems.

'''
def print_roman_numeral(num: int):
    """
    determines and prints the corresponding roman numeral for the given num

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
    """
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
    elif num==10:
        print('X')


'''
Q3. Design a function that takes 2 numbers representing an (x,y) point on a 
graph and prints what quadrant it is in.  RECALL:  quadrants are numbered 
1 through 4 counter clockwise starting at the upper right quadrant.
    
The function should print: '( x# , y# )' where x# and y# are the x,y arguments
if x and y are zero it should then print 'at center'
otherwise if x or y are zero it should print 'on x-axis'
otherwise it should print 'Q#' where # is the quadrant number it is in
'''
def print_quadrant(x: float, y: float):
    ''' This function will print a set of graph coordinates followed by the 
    quadrant that coordinate is in
    
    >>> print_quadrant(0,0)
    ( 0 , 0 )
    at center
    >>> print_quadrant(0,1)
    ( 0 , 1 )
    on y-axis
    >>> print_quadrant(1,0)
    ( 1 , 0 )
    on x-axis
    >>> print_quadrant(1,1)
    ( 1 , 1 )
    Q1
    >>> print_quadrant(-1,1)
    ( -1 , 1 )
    Q2
    >>> print_quadrant(-1,-1)
    ( -1 , -1 )
    Q3
    >>> print_quadrant(1, -1)
    ( 1 , -1 )
    Q4
    '''
    
    print(f'( {x} , {y} ')
    
    if x == 0 and y == 0:
        
        quadrant = 'at center'
    
    elif x == 0:
        
        quadrant = 'on y-axis'
    
    elif y == 0:
        
        quadrant = 'on x-axis'
        
    elif x > 0 and y > 0:
        
        quadrant = 'Q1'
        
    elif x < 0 and y > 0:
        
        quadrant = 'Q2'
        
    elif x < 0 and y < 0:
        
        quadrant = 'Q3'
        
    else:
        
        quadrant = 'Q4'
        
    print(quadrant)




'''
Q4. Design a function that takes two numbers:
one for air temperature (in degrees Celsius) and
one for air pressure (in pounds per square inch, psi) inside a mechanical device
The function should print the message "Error: data not valid",
if the pressure is negative, and then terminates
otherwise it should print a message about the machine's operation
according to the following:
If the temperature is above 300 degrees C or below 5 degrees C, or if the
pressure is above 150psi, the machine is not operating under normal conditions.

If the temperature is above 250 degrees C and the pressure is above 100psi, 
the machine is not operating under normal conditions.
Otherwise, the machine is operating under normal conditions.
'''





'''
Q5. Write a function that takes the number of people coming
    to a picnic and prints the nubmer of packages of hot dogs and buns to buy
    assume: each person will eat 2 hot dogs and
    the number of buns in a package is NUM_BUNS_PER_PACK and
    the number of buns in a package is NUM_DOGS_PER_PACK and
Tip: if you know you need 16 hot dogs and there are 8 buns per pack and
12 dogs per pack, you need to know how many whole bags of each you need, 
plus an extra bag if the whole bags are not quite enough.
Think about how the results of the following expressions help:
16//8 and 16%8
16//12 and 16%12
'''
