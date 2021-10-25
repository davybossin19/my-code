import doctest

def get_multiples(n: int, num: int) -> str:
    ''' This function should return a string list of num multiples of n
    
    precondition: n >= 0
    >>> get_multiples(0, 4)
    ''
    
    >>> get_multiples(1, 4)
    '4'
    
    >>> get_multiples(3, 0)
    '0,0,0'
    
    >>> get_multiples(3, 4)
    '4,8,12'
    
    >>> get_multiples(3, -5)
    '-5,-10,-15'
    '''
    if n == 0:
        return ''
    
    elif n == 1:
        return str(num)
    
    else:
        multiples_of_num = ''
    
        for i in range(1, n):
            multiples_of_num += str(num * i) + ','
        
        multiples_of_num += str(num * (i + 1))
         
        return multiples_of_num
    
def factorial(n: int) -> int:
    ''' This functions calculates and returns the factorial of a given integer
    
    precondition: n >= 0
    
    >>> factorial(0)
    1
    
    >>> factorial(1)
    1
    
    >>> factorial(2)
    2
    
    >>> factorial(3)
    6
    
    >>> factorial(4)
    24
    '''
    
    if n == 0: 
        return 1
    
    else:
        factorial = n
        
        for i in range (n - 1, 0, -1):
            factorial *= i
            
        return factorial
    
def draw_base(tower_size: int, num_levels: int) -> None:
    ''' This function prints the base of the clock tower image. The output
    varies based on the tower_size input and the number of base levels
    
    precondition: tower_size >= 0
    '''
    indent = '  ' 
    min_lines = 4
    total_lines = tower_size + min_lines
    
    for i in range(num_levels):
        print(indent, end = '')
        print('__' * tower_size, end = '') 
        print('___________')
        
        print(' ' + '|', end = '')
        print('__' * tower_size, end = '')
        print('___________' + '|')
    
        for j in range(total_lines):
            print(indent, end = '') 
            print('|' * (total_lines + 1) , end = ' ') 
            print('|' * (total_lines + 1))
    
    
def draw_top(tower_size: int) -> None:
    ''' This function prints the 'top' portion of the tower image. The output 
    scales according to the tower_size argument
    
    precondition: tower_size >= 0
    '''
    
    indent = '   '
    min_lines = 3
    
    total_lines = tower_size + min_lines
    
    print(indent + '|' + '**' * tower_size + '*******' + '|') 
    
    spaces = total_lines
    
    for i in range(1, total_lines + 1):
        slashes = i
        spaces -= 1
        print(indent + '|' + ' ' * spaces + '/' * slashes, end = '') 
        print(' ', end = '') 
        print('\\' * slashes + ' ' * spaces + '|')
        

def draw_face(tower_size: int) -> None:
    ''' This function prints the clock-face portion of the the clock-tower image
    
    precondition: tower_size >= 0
    '''
    extra_lns_base = '~~~~~~~~~~~~~'
    first_last_base = '-------------'
    
    #core of clock towerimage
    clock_ln1 = '|-----------|'
    clock_ln2 = '|@  **^**  @|'
    clock_ln3 = '|  ** | **  |'
    clock_ln4 = '| *   @-->* |'
    clock_ln5 = '|  **   **  |'
    clock_ln6 = '|@  *****  @|'
    clock_ln7 = '|-----------|'
    
    #book end line 1
    print('|' + '--' * tower_size, end = '')
    print(first_last_base + '|')
    
    #loop to print filler lines
    for i in range(tower_size):
        print('|' + '~~' * tower_size, end = '')
        print(extra_lns_base + '|')
    
    #print statements for clock tower core with scalable filler    
    print('|' + tower_size * '~' + clock_ln1 + tower_size * '~' + '|')
    print('|' + tower_size * '~' + clock_ln2 + tower_size * '~' + '|')
    print('|' + tower_size * '~' + clock_ln3 + tower_size * '~' + '|')
    print('|' + tower_size * '~' + clock_ln4 + tower_size * '~' + '|')
    print('|' + tower_size * '~' + clock_ln5 + tower_size * '~' + '|')
    print('|' + tower_size * '~' + clock_ln6 + tower_size * '~' + '|')
    print('|' + tower_size * '~' + clock_ln7 + tower_size * '~' + '|')
    
    #loop to print filler lines
    for i in range(tower_size):
        print('|' + '~~' * tower_size, end = '')
        print(extra_lns_base + '|')
    
    #book end line 2
    print('|' + '--' * tower_size, end = '')
    print(first_last_base + '|')
    

def draw_clock_tower(tower_size: int, num_levels: int) -> None:
    ''' This function calls the helper function that each print a portion of 
    the clock-tower image
    
    precondition: precondition: tower_size >= 0 and num_levels >= 0
    '''
    
    draw_face(tower_size)
    draw_top(tower_size)
    draw_base(tower_size, num_levels)
    
    
    
    

