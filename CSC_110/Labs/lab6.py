import doctest
from typing import List

def sum_even_values(array: List[int]) -> int:
    ''' This function should take a list of integers and retun thge sum of all 
    even numbers in the list.
    
    >>> sum_even_values([])
    0
    >>> sum_even_values([1,3,5])
    0
    >>> sum_even_values([2,4,6])
    12
    >>> sum_even_values([1,2,3,4,5,6])
    12
    >>> sum_even_values([10,100,150])
    260
    >>> sum_even_values([-1,-3,-5])
    0
    >>> sum_even_values([-2,-4,-6,6])
    -6
    >>> sum_even_values([1])
    0
    >>> sum_even_values([2])
    2
    '''
    sum_evens = 0
    for num in array:
        if num % 2 == 0:
            sum_evens += num
    
    return sum_evens


def count_above(array: List[float], bound_val: float) -> int:
    ''' This function should take a list of numbers and a boundary value and 
    return the amount of numbers above the boundary value.
    
    >>> count_above([],2.1)
    0
    >>> count_above([12,4,2,22,-4],2)
    3
    >>> count_above([1.2,2.4,2.7],2.1)
    2
    >>> count_above([1.2,2.4,2.7],5)
    0
    >>> count_above([2.7],2.1)
    1
    >>> count_above([2.4],2.4)
    0
    >>> count_above([2.3],2.4)
    0
    >>> count_above([1.2,2.4,2.7],-2.1)
    3
    >>> count_above([-1.2,-2.4,-2.7],2.1)
    0
    '''
    num_above = 0
    
    for num in array:
        if num > bound_val:
            num_above += 1
            
    return num_above


def add1(array: List[int]) -> List[int]:
    ''' This function should take a list of ints and create and return a new 
    with each value from the original list increased by 1
    
    >>> add1([])
    []
    >>> add1([12, 4, 3, -2])
    [13, 5, 4, -1]
    >>> add1([1,2,3])
    [2, 3, 4]
    >>> add1([-1,-2,-3])
    [0, -1, -2]
    >>> add1([-1.4,2.8,3.97])
    [-0.4, 3.8, 4.97]
    >>> add1([0])
    [1]
    '''
    
    new_list = []
    
    for num in array:
        new_list.append(num + 1)
        
    return new_list


def are_all_even(array: List[int]) -> bool:
    ''' This function should return True of False if all elemnts of the input 
    are even or not:
    
    >>> are_all_even([])
    True
    >>> are_all_even([0])
    True
    >>> are_all_even([1])
    False
    >>> are_all_even([2])
    True
    >>> are_all_even([-1])
    False
    >>> are_all_even([-2])
    True
    >>> are_all_even([2,4,6,8])
    True
    >>> are_all_even([2,4,6,1,8])
    False
    '''
    for num in array[1:]:
        if num % 2 != 0:
            return False
    
    return True
        


