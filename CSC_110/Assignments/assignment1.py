def print_highway_at_night():
    
    '''
    This function should print ASCII art of a highway at night under a full
    moon, the quotation marks are relflectors on mileage markers
    '''
    
    print('    O')
    print('  \'/|\\\'')
    print('  / | \\ ')
    print('\"/  |  \\\"')
    
    
def print_sparkling_diamond():
    
    '''
    This function should print a diamond with quotations as sparkles and dollar 
    signs for effect 
    '''
    
    print('    /\\')
    print('   / \'\\')
    print('  / $$ \\')
    print('  \\ $$ /')
    print('   \\ \"/')
    print('    \\/')
    

def print_logo():
    
    '''
    This function should output alternating pieces of ASCII art with a
    spacer line of " /~~~~~~~~\ " inbetween each drawing. Each piece of art 
    should be displayed two times total
    '''
    
    spacer_line = '/~~~~~~~~\\'
    
    print_highway_at_night()
    print(spacer_line)
    print_sparkling_diamond()
    print(spacer_line)
    print_highway_at_night()
    print(spacer_line)
    print_sparkling_diamond()
    print(spacer_line)    
    
    
#Global constant for miles to kilometres conversion    
KMS_PER_MILE = 1.60934
    
def miles_to_kms(miles: float):
    
    '''
    This function should take a float input and conver that amount of miles to 
    equivalent amount of kilometres. The conversion rate is found in the global 
    constant above the function defintion
    
    Examples:
    >>>miles_to_kms(5.7)
    9.173238 km
    
    >>>miles_to_kms(4)
    6.43736 km
    '''
    
    kms = miles * KMS_PER_MILE
    
    print(kms, 'km')



