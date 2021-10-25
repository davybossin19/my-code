import doctest
from typing import List, Tuple

#Prsents a flights information (origin, destination, duration(hours))
#Where origin and destination != '', duration > 0
Flight = Tuple[str, str, float]

ORIGIN = 0
DESTINATION = 1
DURATION = 2

                   
    
def index_of_smallest(array: list) -> int:
    ''' This function should take a list of values and return the index of the 
    minimum element in the list
    
    Precondition: all values in the list must be comparable to one another
    
    >>> index_of_smallest([])
    -1
    >>> index_of_smallest([1,2,3])
    0
    >>> index_of_smallest([2,1,3])
    1
    >>> index_of_smallest([3,2,1])
    2
    >>> index_of_smallest(['a','b','c'])
    0
    >>> index_of_smallest(['c','a','b'])
    1
    >>> index_of_smallest(['B','c','a'])
    0
    '''
    if array == []:
        index = -1
    
    else:
        min_found = False
        len_array = len(array)
        mini = array[0]
        index = 0
        
        
        for i in array:
            if i < mini:
                mini = i
            
        while index < len_array and not min_found:
            if array[index] == mini:
                min_found = True
            else:
                index += 1
    
    return index

def total_duration(loflights: List[Flight]) -> float:
    ''' this function should take a list of tuples containing flight information
    and return the duration of all flights
    
    >>> total_duration([])
    0
    
    >>> total_duration([('Victoria', 'Mexico City', 5.5), 
    ... ('Vancouver', 'Toronto', 4)])
    9.5
    >>> total_duration([('Victoria', 'Mexico City', 5.5), 
    ... ('Vancouver', 'Toronto', 4),('Hanoi', 'Churchill', 15])
    24.5
    '''
    t_duration = 0
    
    for flight in loflights:
        t_duration += flight[DURATION]
    
    return t_duration


def get_destinations_from(loflights: List[Flight], 
                          depart_city: str) -> List[str]:
    ''' this function should take a list of flights and a departure city and 
    return a list of all unique cities (no repeating elements) 
    that can be flown to from the departure city
    
    >>> get_destinations_from([],'Victoria')
    []
    
    >>> get_destinations_from([], '')
    []
       
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75),
    ... ('Vancouver', 'Toronto', 4), ('Victoria', 'Calgary', 1.5),
    ... ('Victoria', 'Vancouver', 0.5)], '')
    []
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75),
    ... ('Vancouver', 'Toronto', 4), ('Victoria', 'Calgary', 1.5),
    ... ('Victoria', 'Vancouver', 0.5)], 'Victoria')
    ['Vancouver', 'Calgary']
    '''
    dest_cities = []
    
    for flight in loflights:
        
        if (flight[ORIGIN] == depart_city and 
            flight[DESTINATION] not in dest_cities):
            
            dest_cities.append(flight[DESTINATION])
            
    return dest_cities    
    
    
def get_zodiac_signs(lodates: List[Date]) -> List[str]:
    ''' This function should take a list date information tuples and returns a 
    list of the corresponding zodiac signs for those dates 
        
            
        
            
    
        
    
    

