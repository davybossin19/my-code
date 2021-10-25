import doctest
from typing import List

passed = 0
ran = 0


'''
Q1. Design a function that takes a list of integers and an
additional integer.  The function should determine whether the
additional number is contained in the list.
Do not use the builtin in operator.
'''


'''
Q2. Design a function that takes a list of integers and an additional integer as second argument.
The function subtracts the integer from every value in the list.
If the subtraction results in a value below 0,
the element at that position should be set to 0.
'''
def sub_int_from_list(array:List[int], val: int) -> None:
    
    array_len = len(array)
    
    for i in range:
        if array[i] - val < 0:
            array[i] = 0
        else:
            array[i] -= val

# we will look at how to use the print_test function 
# to test functions that mutate a list
def test_minus_val() -> None:
    """ test the minus_val function
    """
    empty = []
    minus_val(empty, 2)
    print_test("minus_val(empty)", empty == [])

    list_345 = [3,4,5]
    minus_val(list_345, 4)
    print_test("minus_val(list_345)", list_345 == [0,0,1])

    list_34neg5 = [3,4,-5]
    minus_val(list_34neg5, -8)
    print_test("minus_val(list_34neg5, -8)", list_34neg5 == [11,12,3])

'''
Q3. Design a function that will take a list of integers and returns the 
smallest number in the list. Your function should assume the list is not empty.
'''
def get_min(loints: List[int]) -> int:
    
    small = loints[0]
    
    for i in loints:
        if  i < small:
            small = i
    
    return small


'''
Q4. Design a function that will take a list of integers and
determines whether the numbers in that list are strictly decreasing by 1
ie. [5,4,3,2] is strictly decreasing by 1
ie. [5,4,3,0] is not strictly decreasing by 1
ie. [5,6,3,2] is not strictly decreasing by 1
ie. [5,6,7,8] is not strictly decreasing by 1
'''


'''
Q5a. Design a function that takes a list of integers and an
additional integer.  The function should return the position
the additional integer is found in the list if it is found, 
otherwise it should return -1 to indicate it is not in the list.
If there are multiple occurances of the value, the function
should return the highest index.
'''



'''
Q5b. redesign Q6a so that if there are multiple occurances of the value, 
the function returns the lowest index.
'''



def print_test(test_name:str, expression:bool):
    '''
    prints test_name followed by 'passed' if expression evaluates to True,
    prints test_name followed by 'failed' if expression evaluates to False
    >>> print_test('test1', True) # doctest: +SKIP
    test1: passed
    >>> print_test('test2', False) # doctest: +SKIP
    test2: failed
    '''
    global ran, passed
    ran += 1
    if expression:
        print(test_name + ': passed')
        passed += 1
    else:
        print(test_name + ': failed')


def main():
    global ran, passed
    
    
    print(passed, '/', ran, 'tests passed')

    