import doctest
from typing import List, Tuple
'''
a tuple to store the date in format(year, month, day)
where year >= 1582, month is a valid month (January to December)
day is a valid day given year and month
'''
Date = Tuple[int, str, int]

YEAR = 0
MONTH = 1
DAY = 2
'''
Presents a flights information (origin, destination, duration)
where origin and destination != '', duration > 0,  duration in hours
'''
Flight = Tuple[str, str, float]

ORIGIN = 0
DESTINATION = 1
DURATION = 2
'''
Presents a flights schedule information ((origin, destination, duration(hours))
,(list of dates for that  specific flight)
'''
Flight_sched_info = Tuple[Flight, List[Date]]

FLIGHT_INFO = 0
FLIGHT_DATES = 1

def multiply_by(array: list, multiplier: int) -> None:
    ''' This function should tkae a list and multiply every element in the list 
    by a given multiplier.
    
    Precondition: All elements in list can be multiplied by an int
    Precondition: multiplier >= 0
    '''
    
    len_arr = len(array)
    
    for i in range(len_arr):
        array[i] *= multiplier
        
        
def are_getting_shorter(lostrs: str) -> bool:
    ''' This function should take a list of strs and determine if the strings
    smaller with each element as you progress through the list.
    
    >>> are_getting_shorter(['','a',''])
    False
    
    >>> are_getting_shorter(['','',''])
    False
    
    >>> are_getting_shorter(['aa','a',''])
    True
    
    >>> are_getting_shorter(['dfnsaf','fdsaa','dd'])
    True
    '''
    len_lostrs = len(lostrs)
    index = 0
    getting_shorter = True
    
    while getting_shorter and index < len_lostrs - 1:
        if len(lostrs[index]) <= len(lostrs[index + 1]):
            getting_shorter = False
        index += 1
        
    return getting_shorter


def get_zodiac_sign(month: str, day: int) -> str:
    ''' This function will take your birth month and birthday and print out
    your zodiac sign.
    
    Precondition: Assumes all dates are valid
    
    >>> get_zodiac_sign('January',20)
    'Aquarius'
    
    >>> get_zodiac_sign('January',31)
    'Aquarius'
    
    >>> get_zodiac_sign('February',15)
    'Aquarius'
    
    >>> get_zodiac_sign('February',18)
    'Aquarius'
    
    >>> get_zodiac_sign('February',19)
    'Pisces'
    
    >>> get_zodiac_sign('February',29)
    'Pisces'
    
    >>> get_zodiac_sign('March',20)
    'Pisces'
    
    >>> get_zodiac_sign('March',21)
    'Aries'
    
    >>> get_zodiac_sign('March',31)
    'Aries'
    
    >>> get_zodiac_sign('April',19)
    'Aries'
    
    >>> get_zodiac_sign('April',20)
    'Taurus'
    
    >>> get_zodiac_sign('April',30)
    'Taurus'
    
    >>> get_zodiac_sign('May',20)
    'Taurus'
    
    >>> get_zodiac_sign('May',21)
    'Gemini'
    
    >>> get_zodiac_sign('May',31)
    'Gemini'
    
    >>> get_zodiac_sign('June',20)
    'Gemini'
    
    >>> get_zodiac_sign('June',21)
    'Cancer'
    
    >>> get_zodiac_sign('June',30)
    'Cancer'
    
    >>> get_zodiac_sign('July',22)
    'Cancer'
    
    >>> get_zodiac_sign('July',23)
    'Leo'
    
    >>> get_zodiac_sign('July',31)
    'Leo'
    
    >>> get_zodiac_sign('August',22)
    'Leo'
    
    >>> get_zodiac_sign('August',23)
    'Virgo'
    
    >>> get_zodiac_sign('August',31)
    'Virgo'
    
    >>> get_zodiac_sign('September',22)
    'Virgo'
    
    >>> get_zodiac_sign('September',23)
    'Libra'
    
    >>> get_zodiac_sign('September',30)
    'Libra'
    
    >>> get_zodiac_sign('October',22)
    'Libra'
    
    >>> get_zodiac_sign('October',23)
    'Scorpio'
    
    >>> get_zodiac_sign('October',31)
    'Scorpio'
    
    >>> get_zodiac_sign('November',21)
    'Scorpio'
    
    >>> get_zodiac_sign('November',22)
    'Sagittarius'
    
    >>> get_zodiac_sign('November',30)
    'Sagittarius'
    
    >>> get_zodiac_sign('December',21)
    'Sagittarius'
    
    >>> get_zodiac_sign('December',22)
    'Capricorn'
    
    >>> get_zodiac_sign('December',31)
    'Capricorn'
    
    >>> get_zodiac_sign('January',19)
    'Capricorn'
    '''
    
    
    if month == 'January':
        if day < 20:
            zodiac_sign = 'Capricorn'
        else:
            zodiac_sign = 'Aquarius'
    
    elif month == 'February':
        if day < 19:
            zodiac_sign = 'Aquarius'
        else:
            zodiac_sign = 'Pisces'
    
    elif month == 'March':
        if day < 21:
            zodiac_sign = 'Pisces'
        else:
            zodiac_sign = 'Aries'
            
    elif month == 'April':
        if day < 20:
            zodiac_sign = 'Aries'
        else:
            zodiac_sign = 'Taurus'
    
    elif month == 'May':
        if day < 21:
            zodiac_sign = 'Taurus'
        else:
            zodiac_sign = 'Gemini'
    
    elif month == 'June':
        if day < 21:
            zodiac_sign = 'Gemini'
        else:
            zodiac_sign = 'Cancer'
    
    elif month == 'July':
        if day < 23:
            zodiac_sign = 'Cancer'
        else:
            zodiac_sign = 'Leo'
            
    elif month == 'August':
        if day < 23:
            zodiac_sign = 'Leo'
        else:
            zodiac_sign = 'Virgo'
            
    elif month == 'September':
        if day < 23:
            zodiac_sign = 'Virgo'
        else:
            zodiac_sign = 'Libra'
    
    elif month == 'October':
        if day < 23:
            zodiac_sign = 'Libra'
        else:
            zodiac_sign = 'Scorpio'    
            
    elif month == 'November':
        if day < 22:
            zodiac_sign = 'Scorpio'
        else:
            zodiac_sign = 'Sagittarius'
    
    else:
        if day < 22:
            zodiac_sign = 'Sagittarius'
        else:
            zodiac_sign = 'Capricorn'
    
    return zodiac_sign


def get_zodiac_signs(lodates: List[Date]) -> List[str]:
    ''' This function should take a list of Date tuples and return a list of 
    corresponding zodiac signs for the those dates
    
    >>> get_zodiac_signs([])
    []
    
    >>> get_zodiac_signs([(1990, 'June', 19)])
    ['Gemini']
    
    >>> get_zodiac_signs([(1990, 'September', 15), 
    ... (1829, 'December', 28), (1845, 'August', 27)])
    ['Virgo', 'Capricorn', 'Virgo']
    '''
    
    new_list = []
    
    for date in lodates:
        new_list.append(get_zodiac_sign(date[MONTH], date[DAY]))
        
    return new_list


def create_lodates(lomonths: List[str], lodays: List[int], 
                   loyears: List[int]) -> List[Date]:
    ''' This function should take a list of months, a list of days and a list of
    months and return a list of dates by combining elements from all three lists
    
    precondition: list items must combine to make valid dates, 
    length of all three lists are equal
    
    >>> create_lodates([],[],[])
    []
    
    >>> create_lodates(['January', 'June'],[20, 10],[1987, 2020])
    [(1987, 'January', 20), (2020, 'June', 10)]
    '''
    len_lomonths = len(lomonths)
    lodates = []
    
    for i in range(len_lomonths):
        date = (loyears[i],lomonths[i],lodays[i])
        lodates.append(date)
    
    return lodates

def contains_month(lodates: List[Date], month: str) -> bool:
    ''' This function takes a list of dtaes and specified month as arguments and 
    returns if any of the given dates contain that months
    
    >>> contains_month([], 'June')
    False
    
    >>> contains_month([(1829, 'December', 28)], 'June')
    False
    
    >>> contains_month([(1829, 'December', 28),(1987, 'January', 20)], 'December')
    True
    '''
    len_lodates = len(lodates)
    month_is_in = False
    index = 0
    
    while not month_is_in and index < len_lodates:
        if lodates[index][MONTH] == month:
            month_is_in = True
        index += 1
    
    return month_is_in


def get_flights_in_month(lo_f_sched_info: List[Flight_sched_info],
                         month: str) -> List[Flight]:
    ''' This function should take a list of flight schedule information tuples 
    and a given month as arguments. The function will return a list of flights 
    that take place in the given month
    
    Precondition: month is valid and first letter capitalized
    
    >>> flight_van_tor = ('Vancouver', 'Toronto', 4)
    
    >>> dates_van_tor = [(2020, 'October', 1), (2020, 'October', 12), 
    ... (2020, 'December', 1), (2020, 'October', 30)]
    
    >>> flight_schedule_van_tor = (flight_van_tor, dates_van_tor)
    
    
    >>> flight_win_mon = ('Winninpeg', 'Montreal', 3)
    
    >>> dates_win_mon = [(2020, 'June', 1), (2020, 'July', 12), 
    ... (2020, 'August', 1), (2020, 'November', 30), (2020, 'October', 12)]
    
    >>> flight_schedule_win_mon = (flight_win_mon, dates_win_mon)
    
    >>> lo_f_sched_info = [flight_schedule_van_tor,flight_schedule_win_mon]
    
    >>> get_flights_in_month(lo_f_sched_info, 'October')
    [('Vancouver', 'Toronto', 4), ('Winninpeg', 'Montreal', 3)]
    
    >>> get_flights_in_month([], 'October')
    []
    
    >>> get_flights_in_month(lo_f_sched_info, 'December')
    [('Vancouver', 'Toronto', 4)]
    
    >>> get_flights_in_month(lo_f_sched_info, 'July')
    [('Winninpeg', 'Montreal', 3)]
    
    >>> get_flights_in_month(lo_f_sched_info, 'January')
    []
    '''
    lo_valid_flights = []
    
    for f_sched in lo_f_sched_info:
        
        if contains_month(f_sched[FLIGHT_DATES], month):
            lo_valid_flights.append(f_sched[FLIGHT_INFO])
        
                
    return lo_valid_flights


              
        


