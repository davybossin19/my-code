import doctest
import time

# we designed this function last lecture
def get_number() -> int:
    ''' repeatedly prompts user for a number >=0
    and returns it as an int
    '''
    prompt = 'enter a whole number >=0: '
    num_as_str = input(prompt)
    while not num_as_str.isdigit():
        num_as_str = input(prompt)

    return int(num_as_str)


'''
Q1. Design a function that will determine and return the largest of a
series of positive numbers entered by a user.  The user enters the values,
one at a time, and enters 0 to indicate there are no more values to enter.
If the user enters an invalid entry (non-integer or number<0),
they are repeatedly prompted until they enter valid data.
'''



'''
Q2. Design a function that will calculate and return the average of a
series of positive numbers entered by a user.  The user enters the values,
one at a time, and enters 0 to indicate there are no more values to enter.
If the user enters an invalid entry (non-integer or number<0),
they are repeatedly prompted until they enter valid data.
If the first number entered by the user is 0, the message
"Error: no data" is printed and the function returns -1.
'''
def get_avg() -> float:
    
    number = get_number()
    count, total = 0, 0
    
    if number == 0:
        print('Error: no data')
        return -1
    
    while number>0:
        total += number
        count += 1
        number = get_number()
    
    print(count)
    print(total)
    
    avg = total/count
    return avg
        

'''
Q3. Design a function called num_chars_before_vowel that takes string 
and counts and returns the number of characters in that string up to the 
first vowel encountered.  
NOTE: we are calling the following vowels - a,e,i,o,u

Use a while loop in your solution!
'''
def num_chars_before_vowel(word: str) -> int:
    ''' This function should loop through a word counting the spaces before the 
    first value
    
    >>> num_chars_before_vowel('')
    0
    
    >>> num_chars_before_vowel('abc')
    0
    
    >>> num_chars_before_vowel('wac')
    1
    
    >>> num_chars_before_vowel('www')
    3
    '''
    
    vowels = ['a','e','i','o','u']
    count = 0
    
    if word == '':
        return 0
    
    while count < len(word) and word[count] not in vowels:
        count +=1
        
    return count
        
            
    


'''
Q4. Design a function that takes an integer and determines whether 
it is prime or not.
NOTE: a number is prime if it is a positive number 
divisible by 2 unique numbers, 1 and itself.
'''
def is_prime(num: int) -> bool:
    
    start = time.time()
    index = int(num ** (1/2))
    print(index)
    
    prime = True
    
    if num % 2 ==0:
        prime = False
        
    else:
        while index > 1:
            if num % index == 0:
                prime = False
            index -= 2
            
    end = time.time()
    print(end - start)
    return prime

'''
Q5. Design a function that takes an integer n and prints the first n prime
numbers that exist with a comma between each.
'''
