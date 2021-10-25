import doctest
import random

MIN_DIE = 1
MAX_DIE = 6
MAX_CHIPS = 100000
MIN_BET   = 20
MAX_BET   = 5000


# TODO: design your function sum_fib_sequence_to_limit here:
def sum_fib_sequence_to_limit(limit: int) -> int:
    ''' This function returns the sum of the fiibonaci sequence up to and 
    including a given limit.
    
    precondition: limit >= 0
    
    >>> sum_fib_sequence_to_limit(0)
    0
    
    >>> sum_fib_sequence_to_limit(1)
    2
    
    >>> sum_fib_sequence_to_limit(2)
    4
    
    >>> sum_fib_sequence_to_limit(21)
    54
    
    >>> sum_fib_sequence_to_limit(20)
    33
    
    >>> sum_fib_sequence_to_limit(144)
    376
    '''
    if limit == 0:
        return 0
    
    x = 0
    y = 1
    z = 1
    total = 0
    
    while z <= limit:
        total += z
        z = x + y
        x = y
        y = z
        
    return total
        

def get_num(min_n: int, max_n:int) -> int:
    ''' This function should take an int as an argument and continue to prompt
    the user until they inter an int equal or greater to min_n and less than or 
    equal to max_n.
    
    Precondition: n >= 0
    '''
    
    user_int = input('Enter a whole number between '+str(min_n)+' and '+ 
                     str(max_n)+ ' inclusive: ')
    
    while not user_int.isdigit() or \
               int(user_int) < min_n or int(user_int) > max_n:
        
        user_int = input('try again - Enter a whole number between '+ 
                         str(min_n)+' and '+ str(max_n)+ ' inclusive: ')
        
    return int(user_int)

def play_craps() -> None:
    """ simulates a game of Craps according to the following algorithm
    - allows the user to buy 0 or more dollars worth of casino chips
    - allows the user to continually play rounds of Craps 
    while they have at least MIN_BET dollars worth of casino chips left and 
    they still want to play again
    - In a round:
    -- the user makes a valid bet
    -- the round of Craps is played and 
    if they win the round they win the amount they bet, 
    otherwise they lose the amount they bet.  
    -- The updated number of dollars worth of casino chips is printed
    
    - when the user is done playing, a cashout message is printed
    """    
    #TODO: complete this function
    chips = buy_casino_chips()
    print('')
    if chips > MIN_BET:
        play = play_again()
        print('')
        while play:
            bet = make_bet(chips)
            chips -= bet
            print('')
            win = play_one_round()
            if win == True:
                chips += 2 * bet
            print('You now have $', chips, 'in chips')
            print('')
            if chips < MIN_BET:
                play = False
                
            else:
                play = play_again()
                print('')
            
        cashout(chips)
        
    else:
        cashout(chips)
        
    
            
        
    

def buy_casino_chips() -> int:
    """ Prompts user for the amount of chips they want to buy in whole dollars.
    Keeps prompting user until a value of at least $0
    but no more than MAX_CHIPS is entered
    """
    #TODO: complete this function
    print('Buy your chips! How many dollars do you want?')
    chips = get_num(0,MAX_CHIPS)
    
    return chips
    


def make_bet(num_chips: int) -> int:
    """ repeatedly prompts user to make a valid bet that is at least MIN_BET 
    but does not go over MAX_BET or num_chips.
    Returns the amount of the valid bet.
    """
    #TODO: complete this function
    print('Make a valid bet.', end =' ')
    if num_chips > MAX_BET:
        bet = get_num(MIN_BET, MAX_BET)
    
    else:
        bet = get_num(MIN_BET, num_chips)
    
    return bet
    

def play_again() -> bool:
    """ Prompts the user to determine whether they want to play again.
    Returns True if the user enters 'yes' and False otherwise.
    """
    play = input('Do you want to play? Enter yes if you do: ')
    
    return play == 'yes'
    #TODO: complete this function
    

def cashout(num_chips: int) -> None:
    """  Prints goodbye message to user:
    Says they are broke if they have less than MIN_BET chips left. 
    Prints how many dollars worth of chips they are cashing out.
    """
    #TODO: complete this function
    if num_chips < MIN_BET:
        print('Sorry, you do not have enough money left to make a bet')
    print('You are cashing out $', num_chips ,'in chips')
    
    
def play_one_round() -> bool:
    """ plays a single round of craps with the user:
    -Rolls a pair of dice to establish a point value.  
    -If the user rolls a 2, 3 or 12, they automatically lose.  
    -If they roll a 7 or 11, they automatically win.  
    -If they roll any other value, this value is called the point value. 
    The user then continues to roll the dice until they roll either
    a 7, in which case they lose, 
    or they roll the point value, in which case they win.
    
    Returns True if the user won the round, False otherwise
    """
    #TODO: complete this function
    auto_lose = [2,3,12]
    auto_win = [7, 11]
    
    first_roll = roll_dice()
    print('You rolled', first_roll)
    
    if first_roll in auto_lose:
        print('You lose!')
        return False
    
    elif first_roll in auto_win:
        print('You win!')
        return True
    
    else:
        point_value = first_roll
        print('Rolling for point:', point_value)
        
        rolls_after = roll_dice()
        print('You rolled', rolls_after)
        
        
        while rolls_after != point_value and rolls_after != 7:
            rolls_after = roll_dice()
            print('You rolled', rolls_after)
        
        if rolls_after == point_value:
            print('You win!')
            return True
        
        else: 
            print('You lose!')
            return False        
        
        
        


def roll_dice() -> int:
    """ simulates the roll of 2 dice and returns the sum of the two
    """
    two_die = roll_one_die() + roll_one_die()
    return two_die

def roll_one_die() -> int:
    """ simulates the roll of a single die and returns the value
    """
    die = random.randint(MIN_DIE, MAX_DIE)
    return die