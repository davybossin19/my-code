import doctest
import math

GRAV_ACCEL  = 9.8

''' 
Q1. Design a function that will take a word and determine whether 
it is plural or not (ends with the letter s)
'''
def is_plural(word: str) -> bool:
    ''' This function will return wheather a word ends with 's'
    
    >>> is_plural('dogs')
    True
    
    >>> is_plural('dog')
    False
    
    >>> is_plural('')
    False
    '''
    if word == '':
        return False
    
    elif word[-1] == 's':
        return True
    else: 
        return False
        

'''
Q2. Design a function that pluralizes a word if it is not already plural
The function should return a pluralized word (s added to the end)
'''
def pluralize(word: str) -> str:
    ''' This function will return a pluralized version of a word, if the word is
    already a plural it will turn the word
    
    precondition: word != ''
    
    >>> pluralize('dog')
    'dogs'
    
    >>> pluralize('dog')
    'dogs'
    
    >>> pluralize('')
    's'
    '''
    
    if not is_plural(word):
        word += 's'
    
    return word

'''
Q3. Design a function that takes a string and determines whether it 
is composed of exactly 2 repeating strings ie. 'abcabc' is a repeating string.
'''
def is_repeating(string: str) -> bool:
    ''' 
    
    >>> is_repeating('abcabc')
    True
    
    >>> is_repeating('')
    True
    
    >>> is_repeating('abcabcd')
    False
    '''
    len_string = len(string)
    
    return string[:len_string // 2] == string[len_string // 2:]
    
'''
Q4. This is a function I left you to complete in a previous lecture
Update this function so it returns the length of the adjacent side.
Design a second function that will return the length of the opposite side.
'''
def print_adjacent_length(hypotenuse: float, angle: float) -> None:
    '''
    calculates and prints the length of the side of a right-angle
    triangle adjacent to given angle in degrees and given hypotenuse length
    Precondition: hypotenuse and angle > 0
    >>> print_adjacent_length(13.2, 60)
    6.6
    >>> print_adjacent_length(28.7, 29.8)
    24.9
    '''
    radians = math.radians(angle) # using built-in radians function
    adjacent = math.cos(radians) * hypotenuse
    print(format(adjacent, '.1f'))
    
def print_opposite_length(hypotenuse: float, angle: float) -> None:
    '''
    calculates and prints the length of the side of a right-angle
    triangle adjacent to given angle in degrees and given hypotenuse length
    Precondition: hypotenuse and angle > 0
    >>> print_opposite_length(10, 45)
    7.1
    >>> print_opposite_length(10, 88)
    10.0
    '''
    radians = math.radians(angle) # using built-in radians function
    opposite = math.sin(radians) * hypotenuse
    print(format(opposite, '.1f'))


'''
Q5. Below is a function that I left you to complete last lecture.
Design another function that takes the distance in meters from a point 
to the ground and a time in seconds.  The function should determine whether 
the object will hit the ground in the given time.
The function should assume that both time and distance are not negative.
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

def will_hit_ground(dist_m: float, time_s: float) -> bool:
    ''' This function will tell you if a falling object would hit the ground in 
    a period of time given its distance from the ground
    
    Precondition: dist_m >=0 and time_s >=0
    
    >>> will_hit_ground(400, 10)
    True
    
    >>> will_hit_ground(550, 10)
    False
    ''' 
    
    return dist_m <= fall_distance(time_s)
