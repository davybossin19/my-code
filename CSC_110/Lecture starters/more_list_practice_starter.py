from typing import List, Tuple
import doctest

# represent a persons information as (name, age)
# where name!='' and age>=0
Person = Tuple[str, int]
NAME = 0
AGE  = 1


'''
Q0. Below are two functions we wrote in a past lecture.
Design another function that takes a list of person tuples in increasing
age/name order and an addtional argument that is also a person tuple.
The function should create and return a new list with all the persons in the
orginal list + the additional argument.
The new list should be increasing age order too.
If there are 2 people of the same age, order by name alphabetically.
'''

def get_first_people(people: List[Person], oldest: Person) -> List[Person]:
    """ creates and returns a list of Person containing only
    those from people who are younger than oldest or
    if they are the same age, name must be before p's name alphabetically
    >>> people = [('Adam', 22), ('Jose', 45), ('Adel', 32), ('Georgia', 32)]
    >>> get_first_people([], ('Jill', 30))
    []
    >>> get_first_people(people, ('Juan', 42))
    [('Adam', 22), ('Adel', 32), ('Georgia', 32)]
    >>> get_first_people(people, ('Bill', 32))
    [('Adam', 22), ('Adel', 32)]
    """
    new_list = []

    for p in people:
        if is_before(p, oldest):
            new_list.append(p)

    return new_list

def is_before(p1: Person, p2: Person) -> bool:
    """ determines whether p1 is before p2 in age or name if age is equal
    returns True if it is, False otherwise
    >>> is_before(('Adam', 30), ('Lizzo', 32))
    True
    >>> is_before(('Adam', 32), ('Lizzo', 32))
    True
    >>> is_before(('Zac', 32), ('Lizzo', 32))
    False
    >>> is_before(('Betty', 40), ('Lizzo', 32))
    False
    """
    return p1[AGE]<p2[AGE] or (p1[AGE]==p2[AGE] and p1[NAME]<p2[NAME])


def insert(people: List[Person], new_person: Person):
    """ creates and returns a list with p inserted into people in order
    of increasing age. If ages are equal, order by name alphabetically.
    Precondition: people is in increasing age order, then alphabetical by name
    >>> insert([], ('Tian', 19))
    [('Tian', 19)]
    >>> insert([('Adam', 22), ('Jose', 25), ('Lizzo', 32)], ('Jill', 19))
    [('Jill', 19), ('Adam', 22), ('Jose', 25), ('Lizzo', 32)]
    >>> insert([('Adam', 22), ('Jose', 25), ('Lizzo', 32)], ('Jill', 25))
    [('Adam', 22), ('Jill', 25), ('Jose', 25), ('Lizzo', 32)]
    >>> insert([('Adam', 22), ('Jose', 25), ('Lizzo', 32)], ('Jill', 33))
    [('Adam', 22), ('Jose', 25), ('Lizzo', 32), ('Jill', 33)]
    """
    new_list = get_first_people(people, new_person)
    
    len_first = len(new_list)
    
    new_list.append(new_person)
    
    people_left = people[len_first:]
    
    new_list += people_left
    
    
    return new_list
    



'''
Q1. Design a function that takes a list of person tuples in no particular order.  
The function should create and return a new list in increasing age order.
'''
def sort_people(people: List[Person]) -> List[Person]:
    
    sorted_people = []
    
    for person in people:
        sorted_people = insert(sorted_people, person)
    
    return sorted_people



'''
Q2. If we call sort_people with a list of 1000 people, in the worst case,
how many times will the following line insert execute: index += 1
'''



'''
Q3. Knowing what you know about loops and nested loops,
which implementations of max would you use in your programs?
'''

def max1(lon: List[int]) -> int:
    biggest = lon[0]
    for num in lon:
        if num>biggest:
            biggest = num
    return biggest


def max2(lon: List[int]) -> int:
    sorted_list = sorted(lon) # builtin sort function
    last = len(lon) - 1
    return sorted_list[0]


def max3(lon: List[int]) -> int: 
    for count in range(num_elements - 1):
        to_remove = min(lon) 
        remove(to_remove) # finds element in the list and removes it
    return lon[0]

'''
Q4. Design a function that will sort a given list of integers.
The function should use a selection sort algorithm:
for each position in the given list, 
-finds the smallest value between the current position 
and the end of the list
-swaps the values at the current position and 
the position of the smallest value
NOTE: this function will mutate the list
TIP: use the functions you wrote in lab as helper functions:
'''
def selection_sort(array: List[int]) -> None:
    
    index = 0
    for num in array:
        
        for j in array[index:]:
            index_of_min = index_of_smallest(array[index:])
            swap(array, index, index + index_of_min)
        
        index += 1
        

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
    >>> index_of_smallest(['b','c','a'])
    2
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

def swap(array: list, index1: int, index2: int) -> None:
    ''' This function should take a list and two index values and the swap the 
    elements at the given indexes
    
    precondition: given values are valid indexes 
    '''
    
    array[index1], array[index2] = array[index2], array[index1]