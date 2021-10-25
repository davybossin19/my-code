import math

def print_longer(string1: str, string2: str):
    ''' This function should take two strings as input and use the len() 
    function of python to evaluate the length of the two strings and print the 
    longer one. If both strings are equal in length it should print the first
    string taken as an argument 'string1'.
    
    >>> print_longer('Burger','Fries')
    Burger
    
    >>> print_longer('I','You')
    You
    
    >>> print_longer('Frank', 'Steve')
    Frank
    '''
    
    if len(string1) >= len(string2):
        print(string1)
    
    else:
        print(string2)
        
def print_real_roots(a: float, b:float, c:float):
    ''' This function should the values a, b and c according to 
    ax^2 + bx + c = 0 and use the quadratic formula to solve for x, if x is a 
    real number.
    
    Precondition: a != 0
    
    >>> print_real_roots(0,2,3)
    ERROR
    
    >>> print_real_roots(1, 3, 10)
    NO REAL ROOTS
    
    >>> print_real_roots(1, -9, 20)
    5.0 , 4.0
    
    >>> print_real_roots(-5, 4, 2)
    -0.348 , 1.148
    
    >>> print_real_roots(1, -10, 25)
    5.0 , 5.0
    
    >>> print_real_roots(12, 5, -3)
    0.333 , -0.75
    '''
    discriminant = b ** 2 - 4 * a * c
    denominator = 2 * a
    
    if discriminant < 0:
        print('NO REAL ROOTS')

    
    elif denominator == 0:
        print('ERROR')
    
    else:
        x1 = (-b + math.sqrt(discriminant))/denominator
        x2 = (-b - math.sqrt(discriminant))/denominator
        
        print(f'{round(x1, 3)} , {round(x2,3)}')
    
    
def print_zodiac_sign(month: str, day: int):
    ''' This function will take your birth month and birthday and print out
    your zodiac sign.
    
    Precondition: Assumes all dates are valid
    
    >>> print_zodiac_sign('January',20)
    Aquarius
    
    >>> print_zodiac_sign('January',31)
    Aquarius
    
    >>> print_zodiac_sign('February',15)
    Aquarius
    
    >>> print_zodiac_sign('February',18)
    Aquarius
    
    >>> print_zodiac_sign('February',19)
    Pisces
    
    >>> print_zodiac_sign('February',29)
    Pisces
    
    >>> print_zodiac_sign('March',20)
    Pisces
    
    >>> print_zodiac_sign('March',21)
    Aries
    
    >>> print_zodiac_sign('March',31)
    Aries
    
    >>> print_zodiac_sign('April',19)
    Aries
    
    >>> print_zodiac_sign('April',20)
    Taurus
    
    >>> print_zodiac_sign('April',30)
    Taurus
    
    >>> print_zodiac_sign('May',20)
    Taurus
    
    >>> print_zodiac_sign('May',21)
    Gemini
    
    >>> print_zodiac_sign('May',31)
    Gemini
    
    >>> print_zodiac_sign('June',20)
    Gemini
    
    >>> print_zodiac_sign('June',21)
    Cancer
    
    >>> print_zodiac_sign('June',30)
    Cancer
    
    >>> print_zodiac_sign('July',22)
    Cancer
    
    >>> print_zodiac_sign('July',23)
    Leo
    
    >>> print_zodiac_sign('July',31)
    Leo
    
    >>> print_zodiac_sign('August',22)
    Leo
    
    >>> print_zodiac_sign('August',23)
    Virgo
    
    >>> print_zodiac_sign('August',31)
    Virgo
    
    >>> print_zodiac_sign('September',22)
    Virgo
    
    >>> print_zodiac_sign('September',23)
    Libra
    
    >>> print_zodiac_sign('September',30)
    Libra
    
    >>> print_zodiac_sign('October',22)
    Libra
    
    >>> print_zodiac_sign('October',23)
    Scorpio
    
    >>> print_zodiac_sign('October',31)
    Scorpio
    
    >>> print_zodiac_sign('November',21)
    Scorpio
    
    >>> print_zodiac_sign('November',22)
    Sagittarius
    
    >>> print_zodiac_sign('November',30)
    Sagittarius
    
    >>> print_zodiac_sign('December',21)
    Sagittarius
    
    >>> print_zodiac_sign('December',22)
    Capricorn
    
    >>> print_zodiac_sign('December',31)
    Capricorn
    
    >>> print_zodiac_sign('January',19)
    Capricorn
    '''
    
    if month == 'January':
        if day < 20:
            print('Capricorn')
        else:
            print('Aquarius')
    
    elif month == 'February':
        if day < 19:
            print('Aquarius')
        else:
            print('Pisces')
    
    elif month == 'March':
        if day < 21:
            print('Pisces')
        else:
            print('Aries')
            
    elif month == 'April':
        if day < 20:
            print('Aries')
        else:
            print('Taurus')
    
    elif month == 'May':
        if day < 21:
            print('Taurus')
        else:
            print('Gemini')
    
    elif month == 'June':
        if day < 21:
            print('Gemini')
        else:
            print('Cancer')
    
    elif month == 'July':
        if day < 23:
            print('Cancer')
        else:
            print('Leo')
            
    elif month == 'August':
        if day < 23:
            print('Leo')
        else:
            print('Virgo')
            
    elif month == 'September':
        if day < 23:
            print('Virgo')
        else:
            print('Libra')
    
    elif month == 'October':
        if day < 23:
            print('Libra')
        else:
            print('Scorpio')    
            
    elif month == 'November':
        if day < 22:
            print('Scorpio')
        else:
            print('Sagittarius')
    
    else:
        if day < 22:
            print('Sagittarius')
        else:
            print('Capricorn')    