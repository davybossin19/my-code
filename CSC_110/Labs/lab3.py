
GST = 0.05
PST = 0.10

def get_longer(str1: str, str2: str) -> str:
    ''' This function should evaluate two strings passed as arguments and return 
    the longer string. If strings are equal in length, the first string passed
    in as an argument will be returned.
    
    >>> get_longer('hey there','hello')
    'hey there'
    
    >>> get_longer('hi','pi')
    'hi'
    
    >>> get_longer('try','exert')
    'exert'
    
    >>> get_longer('','exert')
    'exert'
    
    >>> get_longer('try','')
    'try'
    
    >>> get_longer('','')
    ''
    '''
    if len(str1) < len(str2):
        return str2
    
    else:
        return str1
    

def get_tax(food: float, alcohol: float) -> float:
    ''' This function should take the amount of food and alcohol on a restaurant 
    as two seperate arguments. The function will then calculate the tax on the 
    bill based on GST and PST as defined in global variables. On food there is 
    a 5% GST and 0% PST. On alcohol there is a 5% GST and 10% PST.
    
    Preconditions: food >= 0 and alcohol >= 0
    
    >>> get_tax(28.75, 45.98)
    8.3345
    
    >>> get_tax(0, 97.89)
    14.6835
    
    >>> get_tax(56.68, 0)
    2.834
    '''
    food_tax = food * GST
    alcohol_tax = (alcohol * GST) + (alcohol * PST)
    
    total_tax = food_tax + alcohol_tax
    
    return total_tax


def get_bill_share(food: float, alcohol: float, num_people: int) -> float:
    ''' This function should take the amount of money spent on food, the amount 
    of money spent on alcohol and the number of people splitting a bill, then 
    return the amount each person has to pay(tax included)
    
    Preconditions: food >= 0, alcohol >= 0 and num_people >= 1
    
    >>> get_bill_share(18.93, 0, 2)
    9.93825
    
    >>> get_bill_share(9.89, 10.09, 1)
    21.988
    
    >>> get_bill_share(0, 10.09, 1)
    11.6035
    '''
    total_spent = food + alcohol
    
    tax = get_tax(food, alcohol)
    
    total_bill = total_spent + tax
    
    individual_share = total_bill / num_people
    
    return individual_share
    
    