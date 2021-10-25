import doctest
from typing import List

def multiply_by(array: list, val: int) -> list:
    ''' This function should take a list and an integer value and multiply each 
    element in the list and return the results in the new list
    
    Precondition: all items in last can be * by an int
    
    >>> multiply_by([],0)
    []
    >>> multiply_by([],1)
    []
    >>> multiply_by([],-1)
    []
    >>> multiply_by([],1)
    []
    >>> multiply_by(['ab'],0)
    ['']
    >>> multiply_by([2],2)
    [4]
    >>> multiply_by([2],0)
    [0]
    >>> multiply_by([1,2,3,4],-1)
    [-1, -2, -3, -4]
    >>> multiply_by([45, 'c'],1)
    [45, 'c']
    >>> multiply_by([45, 'c'],2)
    [90, 'cc']
    >>> multiply_by([45, 'c'],0)
    [0, '']
    '''
    new_list = []
    
    for num in array: 
        new_list.append(num * val)
    
    return new_list

def sum_squares(lonums: List[float]) -> float:
    ''' This function should take a list of numbers and return the sum of all 
    the squares of the numbers in the list
    
    >>> sum_squares([])
    0
    >>> sum_squares([1])
    1
    >>> sum_squares([-1])
    1
    >>> sum_squares([-5])
    25
    >>> sum_squares([5])
    25
    >>> sum_squares([0.5])
    0.25
    >>> sum_squares([2, 4, 6])
    56
    >>> sum_squares([2, 4, 0.5])
    20.25
    >>> sum_squares([-5, 4])
    41
    '''
    sum_sq = 0
    
    for num in lonums:
        sum_sq += num ** 2
    
    return sum_sq

def find_biggest(lonums: List[float]) -> float:
    ''' This function should return the biggest element in a list of numbers
    
    precondition: len(lonums) >= 1:
    
    >>> find_biggest([1])
    1
    >>> find_biggest([5])
    5
    >>> find_biggest([-1])
    -1
    >>> find_biggest([0])
    0
    >>> find_biggest([1,2])
    2
    >>> find_biggest([-4,-1])
    -1
    >>> find_biggest([1,77, 9])
    77
    '''
    
    max_num = lonums[0]
    
    for num in lonums:
        if num > max_num:
            max_num = num
    
    return max_num

def remove_starts_with(lostrs: List[str], prefix: str) -> List[str]:
    ''' This function should take a list of strings and string prefix and return 
    a list of all strings that do not begin with the prefix. The prefix check is
    not case_sensitive
    
    >>> remove_starts_with([],'n')
    []
    >>> remove_starts_with([],'N')
    []
    >>> remove_starts_with(['n'],'n')
    []
    >>> remove_starts_with(['n'],'N')
    []
    >>> remove_starts_with(['N'],'n')
    []
    >>> remove_starts_with(['n'],'')
    ['n']
    >>> remove_starts_with(['n','a'],'n')
    ['a']
    >>> remove_starts_with(['n', 'A'],'N')
    ['A']
    >>> remove_starts_with(['n', 'a', 'B'],'n')
    ['a', 'B']
    >>> remove_starts_with(['Fred', 'George'],'fr')
    ['George']
    >>> remove_starts_with(['Fred', 'George', 'Harry', 'Hermoine'],'h')
    ['Fred', 'George']
    '''
    new_list = []
    prefix = prefix.lower()
    len_prefix = len(prefix)
    
    if prefix == '':
        return lostrs
    
    for cur_str in lostrs:
        if prefix != cur_str[0:len_prefix].lower():
            new_list.append(cur_str)
            
    return new_list


def contains_multiples(loints: List[int], val: int) -> bool:
    ''' This function should take a list of ints and a int value and return True
    or False dependent on if all elements of the list are a multiple of the 
    given value.
    
    >>> contains_multiples([],1)
    False
    
    >>> contains_multiples([1],0)
    False
    
    >>> contains_multiples([1],1)
    True
    
    >>> contains_multiples([-1],1)
    True
    
    >>> contains_multiples([5, 10, 15, 20, 25],5)
    True
    
    >>> contains_multiples([2, 4, 6, 8, 10],5)
    False
    
    >>> contains_multiples([5, 9, 15, 20, 25],5)
    False
    
    >>> contains_multiples([-5, -10, -15, -20, -25],5)
    True
    '''
    all_multi = True
    
    if val == 0 or loints == []:
        all_multi = False
    
    i = 0
    len_loints = len(loints)
    
    while all_multi and i < len_loints:
        if loints[i] % val != 0:
            all_multi = False
            
        i += 1
        
    return all_multi
    

def are_all_longer(lostrs: List[str], len_val: int) -> bool:
    ''' This function should determine if every string in a given list has a 
    length longer than a given value.
    
    precondition: len_val >= 0
    
    >>> are_all_longer([], 0)
    False
    >>> are_all_longer([], 1)
    False
    >>> are_all_longer([], 0)
    False
    >>> are_all_longer(['a', 'b', 'c'], 0)
    True
    >>> are_all_longer(['a', 'b', 'c'], 1)
    False
    >>> are_all_longer(['aa', 'bb', 'cc'], 1)
    True
    >>> are_all_longer(['aa', 'bb', 'cc'], 2)
    False
    >>> are_all_longer(['aa', 'bb', 'cc'], -2)
    True
    '''
    
    longer = True
    i = 0
    len_lostrs = len(lostrs)
    
    if lostrs == []:
        longer = False
    
    while longer and i < len_lostrs:
        if not len(lostrs[i]) > len_val:
            longer = False
        i += 1
        
    return longer
    