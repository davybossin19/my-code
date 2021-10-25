def print_my_info():
    
    ''' 
    This function should print out basic information about myself
    >>>print_my_info()
    >>>My name is Davy.
       I am 21 years old.
       Here is some math: 19/21 is 0.9047619047619048
    '''
    my_name = 'Davy'
    
    my_age = 21
    
    fave_number = 19
    
    fave_divided_by_age = fave_number/my_age
    
    print('My name is', my_name +'.')
    
    print('My favourite number is', str(fave_number) + '.')
    
    print('I am', my_age, 'years old.')
    
    print('Here is some math:', str(fave_number) + '/' + str(my_age), 'is', 
          fave_divided_by_age)
    
    
def print_sum(value1: float, value2: float):
    
    '''
    This function should take the input of two floats and print the sum
    For example:
    >>>print_sum(4.3, 4.8)
    >>>9.1
    
    >>>print_sum(5, 4)
    >>>9
    '''
    sum_value = value1 + value2
    
    print(sum_value)
