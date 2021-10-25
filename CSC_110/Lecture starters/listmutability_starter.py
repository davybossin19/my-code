import doctest
from typing import List


passed = 0
ran = 0

'''
Q1. Design a function that will take a list of integers and
changes the first element in the given list to it's negated value.
ie. if the value is 8, change it -8, 
if the value is -2 change it to 2.
'''
def negate_first(loints: List[int]) -> None:
    '''
    >>> negate_fi
    '''
    if loints != []:
        loints[0] *= -1


'''
Q2a. What is the output of the following code given the definition of foo below.
Documentation and type hints omitted intentionally.

list1 = [8, 3, 4, 6]
foo(list1, 5)
print(list1)

'''
def foo(lon, num):
    for n in lon:
        if (num > n):
            n=num

'''
Q2b. What is the output of the following code given the definition of bar below.
Documentation and type hints omitted intentionally.

list2 = [8, 3, 4, 6]
print(list2)
bar(list2, 5)
print(list2)

'''
def bar(lon, num):
    index = 0
    for n in lon:
        if (num > n):
            lon[index] = num
        index += 1
        


'''
Q3. Design a function that will take a list of integers and
adds one to every element in the given list.
'''


'''
Q4a. Design a function that will take a list of integers and change
every value in that list to it's absolute value
DO not use the built in abs function.

Q4b. Design a second version of this function that does use the built-in abs function
'''


'''
Q5. Design a function that takes a list of integers and an
additional integer.  The function should determine whether the
additional number is contained in the list.
Do not use the builtin in operator.
'''
    


'''
Q6. Design a function that takes a list of integers and an additional integer as second argument. 
The function subtracts the integer from every value in the list. 
If the subtraction results in a value below 0, 
the element at that position should be set to 0. 
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
    
    doctest.testmod()