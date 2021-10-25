from math import sqrt

"""
Q1. The following code attempts to print the total price
of a group of items I would like to buy followed by
the amount of money I will have left in my wallet.
My wallet started with 200 dollars.

There are a few things wrong with this program.
What do you think is wrong and how would you fix them?
"""

#print('total of item prices:', 3+4+6+14)
#print('wallet balance:', 200- 3+4+6+14)


"""
Q2a. Recall from your math classes that the equation for 
the lengths of the sides in a right triangle is:
  a^2 + b^2 = c^2  (using the ^ to indicate "raise to the power of")

Write a program that will print the length of side c of 
a right triangle with side a length as 3 and side length b as 4.  
"""
def print_hypotenuse():
    a = 3
    b = 4
    
    c = sqrt(a**2 + b**2)
    
    return c

"""
Q2b. Update the program you just wrote so it is contained within a function.
Test the function by calling it from the shell.
"""


    
"""
Q2c. complete the function below so it prints the lengths
of all sides of the right triangle.
Try to avoid re-writing code you have already written!



Test the function by calling it from the shell.
Your output should look something like this...

Dimensions of this right triangle:
the short sides are length: 3 and 4
the hypotenuse is length:  5.0
"""
def print_triangle_dimensions():
    a = 3
    b = 4
    
    print("The hypotenuse of the triangle is ", print_hypotenuse())
    print('The short sides are ', a, 'and ', b)

"""
Q3. What does the following code print when uncommented?
Rewrite this code so that it is contained in a function
and both the code and the output makes it more clear
what the program is doing.
Test your function by calling it from the shell

"""
def print_two_values():
    value1 = 3.14 * 3.4 ** 2
    value2 = 2 * 3.14 * 3.4
    print(value1, ',', value2)



'''
Q4. Design a function that prints the area of
a 5.7 acre plot of land in square metres
Assume that 1 acre is 4046.85642 square metres
'''

def print_plot_size():
    acre_value = 5.7
    
    square_metre_value = 5.7 * 4046.85642
    
    return square_metre_value 
    
print(print_plot_size())


