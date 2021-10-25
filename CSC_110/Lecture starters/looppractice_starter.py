import doctest

'''
Q1. Design a function that will take a number representing height and it 
should print a right angle triangle using '*'s that is of the given height
You can assume that size is greater than 0
Examples:
if ht is 2, prints:
*
**
if ht is 3, prints:
*
**
***
'''



'''
Q2. Design a function that will take a number representing height and it 
should print an isosceles triangle using '*'s that is of the given height
You can assume that size is greater than 0
Examples:
if ht is 2, prints:
 *
***
if ht is 3, prints:
  *
 ***
*****
'''
def print_isosceles(ht: int) -> None:
     spaces = ht - 1
     
     for i in range (ht):
          print(spaces * ' ' + i * '*' + '*' + i * '*')
          spaces -= 1



'''
Q3. Design a function that will take a number representing height and it 
should print a diamond using '*'s that is of the given height
You can assume that size is greater than 0
Examples:
if ht is 2, prints:
 *
***
 *
if ht is 3, prints:
  *
 ***
*****
 ***
  *
'''
def print_diamond(ht: int) -> None:
     
     spaces = 1
     stars = ht * 2 - 3
     
     print_isosceles(ht)
     
     for i in range(ht - 1):
          print(spaces * ' ' + stars * '*')
          spaces += 1
          stars -= 2


'''
Q4. Design a function that will take a number representing the size 
and prints a pattern of slashes as demonstrated in the examples below 
relative to the given size.
You can assume that size is greater than 0
Examples:
if size is 1, prints:
/
if size is 3, prints:
///
//\
/\\
if size is 4, prints:
////
///\
//\\
/\\\
'''
