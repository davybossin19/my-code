def print_name_age_v1() -> None:
    ''' This function takes a name and age as an input and prints out a greeting
    corrsponding to the age input.
    
    Precondition: Age input must be an int
    '''
    
    name = input('What is your name: ')
    age = int(input('What is your age: '))
              
    if age >= 65:
        age_category = 'senior'
    
    elif age >= 18:
        age_category = 'adult'
    
    else:
        age_category = 'child'
        
    print('hello',name,age_category)
    

def print_name_age_v2() -> None:
    ''' This function takes a name and age as an input and prints out a greeting
    corrsponding to the age input. If the age entered is invalid, a 
    corresponding message will be printed
    '''
    
    name = input('What is your name: ')
    age = input('What is your age: ')
    
    if age.isdigit():
        
        if int(age) >= 65:
            age_category = 'senior'
        
        elif int(age) >= 18:
            age_category = 'adult'
        
        else:
            age_category = 'child'
            
        print('hello',name,age_category)
    
    else:
        print(name,'you are lying about your age')


def get_num(n: int) -> int:
    ''' This function should take an int as an argument and continue to prompt
    the user until they inter an int equal or greater to n.
    
    Precondition: n >= 0
    '''
    
    user_int = input('Enter your age as a whole number: ')
    
    while not user_int.isdigit() or int(user_int) < n:
        user_int = input('Enter your age as a whole number: ')
    
    return int(user_int)


def print_name_age_v3() -> None:
    ''' This function should print out the name and age category based on a user
    input. This function will call the get_num function to esnsure a valid age 
    is entered
    '''
    name = input('What is your name: ')
    age = get_num(0)
    
    if int(age) >= 65:
        age_category = 'senior'
    
    elif int(age) >= 18:
        age_category = 'adult'
    
    else:
        age_category = 'child'
        
    print('hello',name,age_category)