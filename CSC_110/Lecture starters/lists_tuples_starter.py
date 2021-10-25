import doctest
from typing import List, Tuple

#represents a person's information as (name, age)
Person = Tuple[str, int]
NAME = 0
AGE = 1

'''
Q1. Design a function that takes a list of tuples and prints 
the first element of every tuple.
'''
def print_tuple(arr: List[tuple]):
    
    for cur_tuple in arr:
        if cur_tuple != ():
            print(cur_tuple[0], end=',')



'''
Q2. Design a function that takes a list of tuples where each tuple contains
the name and age of a person.  The function should print the information on 
for each person represented in the list.
'''
def print_age_info(lotuples: List[Person]) -> None:
    ''' This function should print the name and age according to the 
    corresponding tuple in a list of people
    >>> print_age_info([('Julia', 23)]
    '''
    for person in lotuples:
        print(person[NAME],':', person[AGE])



'''
Q3. Design a function that takes a list of tuples and an additional tuple as 
arguments. Each tuple contains the name and age of a person.
The function should return a list of only those tuples in the list who are 
younger than the age of the person represented in the additional argument.
If they are the same age, tie should be broken by alphabetical order of names
'''
def get_people_before(lotuples: List[Person], reference: Person) -> List[Person]:
    '''
    >>> get_people_before([('Shane', 19),('Connor', 17),('Mark', 10),
    ('Jill', 20)],('Cane', 17))
    '''
    new_list = []
    
    for person in lotuples:
        if person[AGE] < reference[AGE]:
            new_list.append(person)
            
        elif person[AGE] == reference[AGE]:
            if person[NAME] < reference[NAME]:
                new_list.append(person)
                
    return new_list
            


'''
Q4. Design a function that takes a list of person tuples in increasing age order
and an addtional argument that is also a person tuple.  
The function should create and return a new list with all the persons in the
orginal list + the additional argument.  
The new list should be increasing age order too.
If there are 2 people of the same age, order by name alphabetically.
'''

def add_person(lopeople: List[Person], new_person: Person) -> List[Person]:
    new_list = []
    
    for person in lopeople:
        if person[AGE] < new_person[AGE]:
            new_list.append(person)
            
        elif person[AGE] == new_person[AGE]:
            if person[NAME] < new_person[NAME]:
                new_list.append(person)
                
    new_list.append(new_person)
    
    for person in lopeople:
        if person[AGE] > new_person[AGE]:
            new_list.append(person)
            
        elif person[AGE] == new_person[AGE]:
            if person[NAME] > new_person[NAME]:
                new_list.append(person)
                
    return new_list