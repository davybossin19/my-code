SQR_METERS_PER_ACRE = 4046.85642

def acres_to_sqr_meters(acre: float):
    '''
    Compute the conversion of acres to square meters
    >>>acres_to_sqr_meters(5.7)
    '''

    sqr_meters = acres * SQR_METERS_PER_ACRE
    print('Area is: ', sqr_meters, 'm^2')
    
'''
Q1a. The function definition above is a solution to the problem I left you
with at the end of last lecture.  
How can we make this function easier for some reading it to quickly 
comprehend what the function does.
'''

def cheer(best_team: str):
    '''
    This function will print out 'Go <best_team>!'
    >>>best_team_cheer(Patriots)
    >>>Go Patriots!
    '''
    
    print('Go', best_team + '!')
    

'''
Q1b. The acres_to_sqr_meters function is not very versatile - 
it will only calculate the square meters for 5.7 acres!  
Edit the function so that it will calculate the square meters
for ANY non-negative number of acres.
'''


'''
Q2. Design a function that will take the name of the best team and 
print out a cheer for that team.
'''

def cheer(best_team: str):
    '''
    This function will print out 'Go <best_team>!'
    >>>best_team_cheer(Patriots)
    >>>Go Patriots!
    '''
    
    print('Go', best_team + '!')

'''
Q3. Design a function called print_bill that prints a bill for 
an article of clothing that is $87.98 before taxes.
The bill should include the following items:
 the price, the PST amount, the GST amount, and the total bill
prints the price of the article including provincial sales
NOTE: PST is provincial sales tax at 7%
      GST is goods and services tax at 5%
'''
GST = 0.07

PST = 0.05

def print_bill(price: float):
    
    '''
    This function will take the price of an item and print out the price, gst,
    pst and the total cost
    >>>print_bill(50)
    >>>Item price: $50
       Item GST: $3.5000000000000004
       Item PST: $2.5
       Total price: $56.0

    '''
    
    item_gst = GST*price
    
    item_pst = PST*price
    
    total_price = price + item_gst + item_pst
    
    print('Item price: $' + str(price))
    print('Item GST: $' + str(item_gst))
    print('Item PST: $' + str(item_pst))
    print('Total price: $' + str(total_price))

'''
Q4. Design a function that will take a person's name and age and will 
print a personalized message for that person.
For example, if we call the function as: welcome('Amy', 21)
the function should print:  Welcome Amy! Amy's 21
'''



'''
Q5. Design a function that takes an item weight in kilograms and 
calculates the corresponding weight in pounds and prints the 
result with 2 significant figures on the screen.  
We assume a conversion rate of 2.2 pounds per kilogram. 
'''



