import doctest

LOW_TEMP_LIMIT = 5
MID_TEMP_LIMIT  = 250
HIGH_TEMP_LIMIT = 300

LOW_PRESS_LIMIT  = 0
MID_PRESS_LIMIT  = 100
HIGH_PRESS_LIMIT = 150

'''
Q1.
if millions_won is set to 9 and age is set to 66,
which expressions below will evaluate?


if millions_won is set to 9 and age is set to 65,
which expressions below will evaluate?


if millions_won is set to 11 and age is set to 65,
which expressions below will evaluate?


if millions_won is set to 11 and age is set to 66,
which expressions below will evaluate?


if millions_won>10 or age>65:
    print('retire')

============================================================
if mm_of_rain is set to 10 and walking_minutes is set to 30
which expressions below will evaluate?


if mm_of_rain is set to 10 and walking_minutes is set to 1
which expressions below will evaluate?


if mm_of_rain is set to 0 and walking_minutes is set to 30
which expressions below will evaluate?


if mm_of_rain is set to 0 and walking_minutes is set to 1
which expressions below will evaluate?


if mm_of_rain>1 and walking_minutes>2:
    print('bring umbrella')

'''


'''
Q2. You were asked to design a function according to the specification below.
The function design below has errors in it.
Run doctest.testmod() to help find the errors and fix them.

The function should take two numbers:
one for air temperature (in degrees Celsius) and
one for air pressure (in pounds per square inch, psi) inside a mechanical device
The function should print the message "Error: data not valid",
if the pressure is negative, and then terminates
otherwise it should print a message about the machine's operation
according to the following:
If the temperature is above 300 degrees C or below 5 degrees C, or if the
pressure is above 150psi, the machine is not operating under normal conditions.

If the temperature is above 250 degrees C and the pressure is above 100psi,
the machine is not operating under normal conditions.
Otherwise, the machine is operating under normal conditions.
'''

def print_machine_status(temp: float, press: float):
    '''
    prints a machine status given temp in celcius and press in PSI
    >>> print_machine_status(LOW_TEMP_LIMIT - 1, LOW_PRESS_LIMIT-1)
    Error: data not valid
    
    >>> print_machine_status(LOW_TEMP_LIMIT, LOW_PRESS_LIMIT-1)
    Error: data not valid
    
    >>> print_machine_status(MID_TEMP_LIMIT, LOW_PRESS_LIMIT-1)
    Error: data not valid
    
    >>> print_machine_status(MID_TEMP_LIMIT + 1, LOW_PRESS_LIMIT-1)
    Error: data not valid
    
    >>> print_machine_status(HIGH_TEMP_LIMIT - 1, LOW_PRESS_LIMIT-1)
    Error: data not valid
    
    >>> print_machine_status(HIGH_TEMP_LIMIT, LOW_PRESS_LIMIT-1)
    Error: data not valid


    >>> print_machine_status(HIGH_TEMP_LIMIT+1, HIGH_PRESS_LIMIT)
    abnormal conditions

    >>> print_machine_status(LOW_TEMP_LIMIT-1, HIGH_PRESS_LIMIT)
    abnormal conditions

    >>> print_machine_status(HIGH_TEMP_LIMIT, HIGH_PRESS_LIMIT+1)
    abnormal conditions

    >>> print_machine_status(MID_TEMP_LIMIT+1, MID_PRESS_LIMIT+1)
    abnormal conditions

    >>> print_machine_status(MID_TEMP_LIMIT, MID_PRESS_LIMIT)
    normal conditions
    '''
    if press<0:
        print('Error: data not valid')
    elif (temp < LOW_TEMP_LIMIT or 
          temp > HIGH_TEMP_LIMIT and press > HIGH_PRESS_LIMIT):
        print('abnormal conditions')
    elif temp > MID_TEMP_LIMIT or press > MID_PRESS_LIMIT:
        print('abnormal conditions')
    else:
        print('normal conditions')


''' Q3. Design a function called print_test that takes 2 arguments:
the name of a test as a string and a boolean expression and prints a report.
If the boolean expression evaluates to True, the function should print:
    'test 1 : passed', where 'test 1' is the name of the test
If the boolean expression evaluated to False, the function should print:
    'test 2 : failed', where 'test 2' is the name of the test
'''
def print_test(test_string: str, boolean_exp: bool):
    ''' This function should take a string as the name of the test and boolean 
    expression and print whether the test passed or failed
    
    >>> print_test('test 1', True)
    test 1 : passed
    
    >>>
    
    '''
    if boolean_exp == True:
        print(test_string,': passed')
        
    else:
        print(test_string,': passed')

'''
Q4. Design a function called get_num_teams that takes 2 arguments in this order:
the number of people to be split into teams and the maximum team size.
The function should assume these arguments are greater than zero.
The function should calculate and print the number of teams needed
to split the given number of people evenly with the given maximum team size.
Teams do not have to be the maximum size, but cannot be any bigger.

If the function is called as: get_team_sizes(9, 9)
the function should print: 'teams: 1'
as only 1 team would need to be made to place all 9 people on team
with a maximum of 9 teammates on a team.

If the function is called as: get_num_teams (21, 9)
the function should print: 'teams: 3'
as 3 teams would need to be made to place all 21 people on a team with a maximum of 9 teammates on a team.

If the function is called as: get_num_teams (22, 9)
the function should print: 'teams: 3'
as 3 teams would need to be made to place all 22 people on a team with a maximum of 9 teammates on a team.
'''


'''
Q5. design a function that takes two numbers and prints the one
    with the largest absolute value.
    It should print equal if their absolute values are the same.
It should print the given value, not the absolute value.
Tip: there is a built-in abs function in Python.
    '''
