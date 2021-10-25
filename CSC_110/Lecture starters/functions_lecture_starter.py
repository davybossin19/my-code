import doctest
import math

GRAV_ACCEL = 9.8

'''
Q0. Below is a function that we designed in a past lecture.
Design a function that takes the distance in meters from a point to the ground
and a time in seconds.  The function should determine whether the object will
hit the ground in the give time.
The fucntion should assume that both time and distance are not negative.
'''

def fall_distance(time:int) -> float:
    '''
    returns the distance in meters an object
    would fall in given time in seconds
    >>> fall_distance(-10)
    -1
    >>> fall_distance(0)
    0.0
    >>> fall_distance(10)
    490.00000000000006
    '''
    if time<0:
        return -1

    distance = 1/2 * GRAV_ACCEL * time ** 2

    return distance

'''
Q1. Below are two functions that we left you to design last lecture.
Design a new fuction that takes the length of the hypotenuse of a 
right triangle and the angle in degrees of one of the non-right angle.  
The function should calculate and return the perimeter of the triangle.
Your function can assume the argument values give and > 0
''' 

def get_adjacent_length(hypotenuse:float, angle:float) -> float:
    '''
    calculates and returns the length of the side of a right-angle
    triangle adjacent to given angle in degrees and given hypotenuse length
    
    Precondition: hypotenuse and angle > 0    
    >>> get_adjacent_length(13.2, 60)
    6.600000000000001
    >>> get_adjacent_length(28.7, 29.8)
    24.904868511688246
    '''
    radians = math.radians(angle) # using built-in radians function
    adjacent = math.cos(radians) * hypotenuse
    return adjacent

def get_opposite_length(hypotenuse:float, angle:float) -> float:
    '''
    calculates and returns the length of the side of a right-angle
    triangle opposite the given angle in degrees and given hypotenuse length
    
    Precondition: hypotenuse and angle > 0    
    >>> get_opposite_length(12.8, 60)
    11.085125168440815
    >>> get_opposite_length(24.9, 14.5)
    6.234462100955591
    '''
    radians = math.radians(angle)
    opposite = math.sin(radians) * hypotenuse
    return opposite

def get_perimeter(hypotenuse: float, angle: float) -> float:
    ''' This function should return the perimeter of a right-angle triangle 
    given the hypotenuse and angle
    
    >>> get_perimeter(5,19)
    11.35543
    '''
    opposite = get_opposite_length(hypotenuse,angle)
    adjacent = get_adjacent_length(hypotenuse,angle)
    
    perimeter = hypotenuse + opposite + adjacent
    
    return perimeter
    

'''
Q2. Design a  fuction that takes the length of the hypotenuse of a triangle
and the angle in degrees of one of the non-right angle.  The function
should print the name of the longer side, 'adjacent' or 'opposite'.  
If sides are less than 0.01 difference of each other it should print 'equal'
Your function must make use of the functions you have already written. 
Your function can assume the argument values given are larger than 0
''' 

def print_longer_side(hypotenuse: float, angle: float) -> None:
    ''' This function should take the length of the hypotenuse of a triangle
    and the angle in degrees of one of the non-right angle.  The function
    should print the name of the longer side, 'adjacent' or 'opposite'.  
    If sides are less than 0.01 difference of each other it should print 'equal'
    
    >>>


    
    '''
    opposite = get_opposite_length(hypotenuse,angle)
    adjacent = get_adjacent_length(hypotenuse,angle)
    
    if abs(opposite - adjacent) < 0.01:
        print('Equal')
    
    elif opposite > adjacent:
        print('opposite')
    
    else:
        print('adjacent')
    
    

''' 
Q3. design a function that takes the number of hours an
employee worked in a day and their hourly wage
and returns their total pay
You can assume the number of hours will not be <0 or >24
and that the wage will not be negative.
If they work over 8 hours, you should pay them
1.5 times their wage for all time over 8 hours.
'''




'''
Q4. Design a function called phone_charges that takes the following 
arguments in the given order:
-the basic monthly charge for a cell phone plan (in dollars) that includes
100 free minutes of air time – do not assume that charge is an integer value
-the total number of minutes of air time used in a month (including the 
free minutes included in the basic plan) – assume this is a whole number
-the cost per minute in dollars (ie, 0.20 represents 20 cents per minute) 
of air time beyond the 100 minutes included in the plan

The function should return the calculated phone charges according the 
following specification:
-If the basic monthly charge, total number of minutes used, or cost per 
minute of additional air time is negative, your function must print the 
message: “Error, arguments not valid" and return -1.
-If the arguments were not invalid, your function must return the total 
dollar amount of the cell phone charges in the month.  
The total charges are computed as the basic monthly charge plus a system 
access fee of $5.95 plus the cost of airtime minutes beyond those included 
in the basic plan, if any.  An environmental charge of 7.95 is added to the 
total charges to get the total bill.
Lastly, a 7% tax is added to total bill.
'''

