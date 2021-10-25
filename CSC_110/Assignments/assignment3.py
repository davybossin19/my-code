
UNDER_FIVE_POUND_RATE = 8.50
UNDER_TWENTY_POUND_RATE = 16
ADDL_PER_POUND_RATE = 0.80

POTATOES_PER_LB_COST = 3.45
CARROTS_PER_LB_COST = 2.50
BEETS_PER_LB_COST = 4.56

FIRST_RATE = 0.15
SECOND_RATE = 0.20
THIRD_RATE = 0.25

FIRST_BRACKET_CUTOFF = 300
SECOND_BRACKET_CUTOFF = 450

GPA_CUTOFF = 2.0


def extract_letter(phrase: str, position: int) -> str:
    ''' This function should let the user input a string and the postion of the 
    character they would like to extract. The first character in the string will
    have a position of 1.
    
    Precondition: postion >= 1
    
    >>> extract_letter('abc', 1)
    'a'
    >>> extract_letter('abc', 4)
    ''
    >>> extract_letter('abc', 2)
    'b'
    >>> extract_letter('abc', 3)
    'c'
    '''
    if position > len(phrase):
        return ''
    else:
        return phrase[position - 1]
    
    
def get_median(value1: float, value2: float, value3:float) -> float:
    ''' This function should take three numerical values and return the median 
    value
    >>> get_median(4, 4, 7)
    4
    >>> get_median(4, 7, 4)
    4
    >>> get_median(7, 4, 4)
    4
    >>> get_median(5, 5, 5)
    5
    >>> get_median(10, 9, 8)
    9
    >>> get_median(10, 8, 9)
    9
    >>> get_median(9, 10, 8)
    9
    >>> get_median(9, 8, 10)
    9
    >>> get_median(8, 10, 9)
    9
    >>> get_median(8, 9, 10)
    9
    >>> get_median(9.49, 10.43, 8.45)
    9.49
    >>> get_median(-76, -8, -10)
    -10
    '''
    #cases where value1 is the median
    if (value1 >= value2 and 
        value1 <= value3 or 
        value1 >= value3 and
        value1 <= value2):
        
        median = value1
        
    #cases where value2 is the median
    elif (value2 >= value1 and 
          value2 <= value3 or 
          value2 >= value3 and
          value2 <= value1):
        
        median = value2
    
    #all other cases can be covered with an else statement    
    else:
        median = value3
        
    return median


def calc_shipping(lbs: float) -> float:
    ''' This function should take the weight of an item and calulate the cost of
    its shipping. For 5 pounds or less, the cost is $8.50 flat. Between 5 and 20
    lbs is $16 flat. If the package is 20lbs or greater, there is a flat charge
    of $16 and an addition cost of $0.80 per lb
    
    Precondition: lbs > 0
    
    >>> calc_shipping(1)
    8.5
    
    >>> calc_shipping(5)
    8.5
    
    >>> calc_shipping(7.7)
    16
    
    >>> calc_shipping(20)
    32.0
    
    >>> calc_shipping(22.35)
    33.88
    '''
    if lbs >= 20:
        shipping_cost = UNDER_TWENTY_POUND_RATE + (ADDL_PER_POUND_RATE * lbs)
    
    elif lbs >  5:
        shipping_cost = UNDER_TWENTY_POUND_RATE
        
    else:
        shipping_cost = UNDER_FIVE_POUND_RATE
        
    return shipping_cost


def calc_grocery_charge(lbs_potatoes: float, lbs_carrots: float, 
                        lbs_beets: float) -> float:
    ''' This function should take the amount of potatoes, carrots and beets 
    someone purchases from Schrute Farms and return the total cost of their 
    purchases including shipping
    
    precondition: at least one input > 0 and no inputs < 0
    
    >>> calc_grocery_charge(4.2, 3.1, 5.5)
    63.32
    
    >>> calc_grocery_charge(100.22, 5.43, 8.37)
    504.7172
    
    >>> calc_grocery_charge(0, 5.43, 8.37)
    67.7422
    '''
    grocery_cost = ((lbs_potatoes * POTATOES_PER_LB_COST) + 
                  (lbs_carrots * CARROTS_PER_LB_COST) + 
                  (lbs_beets * BEETS_PER_LB_COST ))
    
    total_weight = lbs_potatoes + lbs_carrots + lbs_beets
    
    shipping_cost = calc_shipping(total_weight)
    
    total_cost = shipping_cost + grocery_cost
    
    return total_cost


def calc_tax(paycheck_amt: float) -> float:
    ''' This function should calculate the total tax that should be deducted off
    a persons paycheque.
    
    precondition: paycheck_amt > 0
    
    >>> calc_tax(600)
    112.5
    
    >>> calc_tax(450)
    75.0
    
    >>> calc_tax(350)
    55.0
    
    >>> calc_tax(300)
    45.0
    
    >>> calc_tax(200)
    30.0
    ''' 
    
    total_first_bracket = FIRST_BRACKET_CUTOFF * FIRST_RATE
    
    total_second_bracket = (total_first_bracket + 
                           (SECOND_BRACKET_CUTOFF - FIRST_BRACKET_CUTOFF)  * 
                            SECOND_RATE)

    
    if paycheck_amt > SECOND_BRACKET_CUTOFF:
        total_tax = (total_second_bracket + 
                    (paycheck_amt - SECOND_BRACKET_CUTOFF) * THIRD_RATE)
        
    elif paycheck_amt > FIRST_BRACKET_CUTOFF:
        total_tax = (total_first_bracket + 
                    (paycheck_amt - FIRST_BRACKET_CUTOFF) * SECOND_RATE)
        
    else: 
        total_tax = paycheck_amt * FIRST_RATE
        
    return total_tax
    

def permitted_to_register(s_gpa: float, good_standing: bool) -> bool:
    ''' This function should calculate is a student is permitted to register 
    based on their GPA and if their in good standing or not. Having either good
    standing, or a GPA at or above 2.0, makes you permitted to register
    
    Precondition: GPA > 0
    
    >>> permitted_to_register(2.0, True)
    True
    
    >>> permitted_to_register(1.9, True)
    True
    
    >>> permitted_to_register(2.0, False)
    True
    
    >>> permitted_to_register(1.8, False)
    False
    '''
    return s_gpa >= GPA_CUTOFF or good_standing == True

    
    