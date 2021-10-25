from typing import List, Tuple
import doctest

# represent a persons information as (name, age)
# where name!='' and age>=0
Person = Tuple[str, int]
NAME = 0
AGE  = 1 


def contains_at_least_one_multiple(lon: List[int], divisor: int) -> bool:
    """ returns True if lon contains at least one number that 
    is a multiple of divisor
    >>> contains_at_least_one_multiple([], 5)
    False
    >>> contains_at_least_one_multiple([3, 4, -6, 5], 15)
    False
    >>> contains_at_least_one_multiple([15, 40, -60, 45], 5)
    True
    >>> contains_at_least_one_multiple([15, 4, -6, 4], 5)
    True
    >>> contains_at_least_one_multiple([3, 4, 20, 4], 5)
    True
    >>> contains_at_least_one_multiple([30, 42, -6, 4], 4)
    True
    >>> contains_at_least_one_multiple([30, 42, -6, 4], 0)
    False
    >>> contains_at_least_one_multiple([0, 0], 0)
    True
    >>> contains_at_least_one_multiple([0, 0], 10)
    True
    """
    # Complete this function...
    index = 0
    num_elements = len(lon)

    while index < num_elements:
        num = lon[index]
        print(num)
        
        index += 1
  

def all_are_multiples(lon: List[int], divisor: int) -> bool:
    """ returns True if lon contains all numbers that are a multiple of divisor
    >>> all_are_multiples([], 5)
    True
    >>> all_are_multiples([3, 4, -6, 5], 15)
    False
    >>> all_are_multiples([15, 40, -60, 45], 5)
    True
    >>> all_are_multiples([15, 4, -6, 4], 5)
    False
    >>> all_are_multiples([3, 4, 20, 4], 5)
    False
    >>> all_are_multiples([30, 42, -6, 4], 2)
    True
    >>> all_are_multiples([30, 42, -6, 4], 0)
    False
    >>> all_are_multiples([0, 0], 0)
    True
    >>> all_are_multiples([0, 0], 10)
    True
    """
    # Complete this function...
    index = 0
    num_elements = len(lon)

    while index < num_elements:
        num = lon[index]
        print(num)
        
        index += 1



def is_multiple(num: int, divisor: int) -> bool:
    """ returns True if num is a multiple of divisor, False otherwise
    >>> is_multiple(0, 0)
    True
    >>> is_multiple(0, 10)
    True
    >>> is_multiple(10, 0)
    False
    >>> is_multiple(10, 20)
    False
    >>> is_multiple(-15, 5)
    True
    """
    return num==0 and divisor==0 or divisor!=0 and num%divisor==0
    #if num == 0 and divisor == 0:
        #return True
    #elif divisor == 0:
        #return False
    #else:
        #return num%divisor==0



"""
Q1. Design a function that will take two lists of integers and
creates and returns a list of tuples that are pairs across the lists.
ie. if the lists are [2, 3, 4] and [5, 6, 7]
the function should return [(2, 5), (3, 6), (4, 7)]

The function should assume the lists are the same length
"""
def zip_list(l1: List[int], l2: List[int]) -> List[Tuple[int, int]]:
    ''' This function should take two lists and generate a list of tuples with a 
    an int from each list at the same index
    
    precondition: len(l1) == len(l2)
    '''
    
    lotuples = []
    len_lists = len(l1)
    
    for i in range(len_lists):
        n_tuple = (l1[i], l2[i])
        lotuples.append(n_tuple)
    
    return lotuples
        

    
"""
Q2. Design a function that will take two lists of integers 
and an additional integer argument.  The function should 
create and return a list of tuples that are pairs across the lists.
If a list is shorter than the other, the tuple gets filled with the 
additional argument.
ie. if the function is called with [2, 3, 4], [5, 6] and 1000
the function should return [(2, 5), (3, 6), (4, 1000)]
"""
def zip_list2(l1: List[int], l2: List[int], val: int) -> List[Tuple[int, int]]:
    len_l1 = len(l1)
    len_l2 = len(l2)
    lotuples = []
    
    if len_l1 != len_l2:
        if len_l1 > len_l2:
                      
            for i in range(len_l2):
                tup = (l1[i], l2[i])
                lotuples.append(tup)
                
            for i in range(len_l1 - len_l2):
                tup = (l1[i + len_l2], val)
                lotuples.append(tup)
        else:
            for i in range(len_l1):
                tup = (l1[i], l2[i])
                lotuples.append(tup)
                
            for i in range(len_l2 - len_l1):
                tup = (l1[i + len_l2], val)
                lotuples.append(tup)
    else:
        lotuples = zip_list(l1, l2)
        
    return lotuples
            
            


"""
Q3. Design a function that will take two lists of integers 
that are in increasing order. The function should 
create and return a list all the values from list1 and list2
in sorted order
ie. if the function is called with [2, 10], [5, 6, 11]
the function should return [2, 5, 6, 10, 11]
"""
def get_sorted_list(loints1: List[int], loints2: List[int]) -> List[int]:
    len_l1 = len(loints1)
    len_l2 = len(loints2)
    
    i = 0
    j = 0
    new_list = []
    
    while i < len_l1 and j < len_l2:
        if loints1[i] < loints2[j]:
            new_list.append(loints[i])
            i += 1
            
        else:
            new_list.append(loints2[j])
            j += 1
    
            
    new_list += loints1[i:] + loints29[j:]     


'''
Q4. Below are two functions we wrote last lecture.
Complete the function insert according to the documentation provided.
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


def insert(people: List[Person], p: Person):
    """ creates and returns a list with p inserted into people in order
    of increasing age. If ages are equal, order by name alphabetically.
    Precondition: people is in increasing age order, then alphabetical by name
    
    >>> people = [('Adam', 22), ('Jose', 25), ('Lizzo', 32)]
    >>> insert([], ('Tian', 19))
    [('Tian', 19)]
    >>> insert(people, ('Jill', 19))
    [('Jill', 19), ('Adam', 22), ('Jose', 25), ('Lizzo', 32)]
    >>> insert(people, ('Jill', 25))
    [('Adam', 22), ('Jill', 25), ('Jose', 25), ('Lizzo', 32)]
    >>> insert(people, ('Xavier', 25))
    [('Adam', 22), ('Jose', 25), ('Xavier', 25), ('Lizzo', 32)]
    >>> insert(people, ('Jill', 33))
    [('Adam', 22), ('Jose', 25), ('Lizzo', 32), ('Jill', 33)]
    """
    # TODO: complete this function
