
import inquirer
import doctest
import numpy as np
import matplotlib.pyplot as plt


def num_periods_in_year(period: str) -> int:
    """
    This function takes a str period value and returns the number of periods
    that occur in a year
    >>> num_periods_in_year('Daily')
    365
    >>> num_periods_in_year('Weekly')
    52
    >>> num_periods_in_year('Monthly')
    12
    >>> num_periods_in_year('Semi-annual')
    2
    >>> num_periods_in_year('Yearly')
    1
    """
    periods_to_num = {'Daily': 365, 'Weekly':52, 'Monthly': 12,
                      'Semi-annual': 2, 'Yearly': 1}

    return periods_to_num[period]

def get_user_c_periods() -> int:
    comp_period_inq = [inquirer.List('Compound Period',
                    message = 'How often does your investment compound?',
                    choices=['Daily','Weekly','Monthly','Semi-annual','Yearly'])]
    answers = inquirer.prompt(comp_period_inq)
    comp_period = answers['Compound Period']

    print("You chose: " + comp_period + "\n")
    return num_periods_in_year(comp_period)

def get_user_a_periods() -> int:
    #additon = input("Will you have a regular additon: (Y/N)? \n").lower().strip()

    # if additon == 'y':
    #     addition_period = [inquirer.List('Additon Period',
    #                     message = 'How often do you contribute your additon?',
    #                     choices=['Daily','Weekly','Monthly','Semi-annual','Yearly'])]
    #
    #     answers2 = inquirer.prompt(addition_period)
    #
    #     return num_periods_in_year(answers2['Additon Period'])

    additon_inq = [inquirer.List('Regular Additon?',
                    message = 'Will you contribute a regular amount?',
                    choices=['Yes','No'])]
    answers = inquirer.prompt(additon_inq)
    addn_y_or_no = answers['Regular Additon?']

    if addn_y_or_no == 'Yes':
        addition_period = [inquirer.List('Additon Period',
                        message = 'How often do you contribute your additon?',
                        choices=['Daily','Weekly','Monthly','Semi-annual','Yearly'])]

        answers2 = inquirer.prompt(addition_period)

        return num_periods_in_year(answers2['Additon Period'])

    else:
        return 500




def calculate_ci() -> float:

    #Arrays for graph
    x = []
    y = []
    z = []

    #Basic stats
    inti_principal = int(input("\n" * 5 +"Enter your starting principal: \n"))
    years = int(input("Years to grow: \n"))
    interest_r = float(input("Enter the annual interest rate: \n"))/100

    c_periods = get_user_c_periods()
    a_periods = get_user_a_periods()

    principal = inti_principal

    total_value = principal

    if a_periods < 500:
        a_amount = int(input('How much is your regular additon: \n'))

    else:
        a_amount = 0

    period_interest = interest_r / c_periods

    if a_amount > 0:
        year_a_periods = 365 // a_periods

    else:
        year_a_periods = 500

    x.append(0)
    y.append(total_value)
    z.append(principal)

    for i in range(years):
            for j in range(1, 366):
                if j %  (365 // c_periods) == 0:
                    #print("c_period:",j)
                    total_value += total_value * period_interest
                if j % year_a_periods == 0:
                    #print('a_period:',j)
                    principal += a_amount
                    total_value += a_amount

            x.append(i+1)
            y.append(total_value)
            z.append(principal)


    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()

    plt.xlim(0, years)
    plt.ylim(inti_principal, total_value)

    plt.title("Compund Interest Earnings")


    plt.fill_between(x, y, z)
    plt.fill_between(x,z, color ='orange')
    plt.show()

    print("\nAfter " + str(years)+ " years your investment is now worth : $"+
          str(round(total_value,2)))
    print("Interest earned : $"+str(round(total_value - principal,2))+'\n')



def main():
    calculate_ci()
if __name__ == "__main__":
    main()
