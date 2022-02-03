"""
Assignment: Basic Function Assignment
Program: basic_function.py
Author: Colby Boell
Last date modified: 02/03/2022

The purpose of this program is to use a basic function to allow user to put in name,
hours, worked and pay rate. It then outputs the information as a string. Using try statements
to ensure we are getting the correct kind of input. Input handling is done in the function in this
program
"""


def hourly_employee_input():  # function to get employee input for name, hours, and hourly pay rate
    # prompts for user to input name
    name = input('Please enter your name: ')
    print(' ')
    # prompts for user input of hours with try statement to ensure valid input
    try:
        hours_worked = int(input('Enter hours worked: '))
        if hours_worked >= 0:
            print('Hours recorded', end=': ')
        else:
            hours_worked = 0
    except ValueError as err:
        hours_worked = 0
        print('Invalid input, hours recorded as 0')
    else:
        print(f'{hours_worked} hours worked')
    finally:
        print(' ')
    # prompts user to enter hourly pay rate, try statement to ensure valid input
    try:
        hourly_pay_rate = float(input('Enter your hourly pay rate: '))
        if hourly_pay_rate >= 0:
            print('Hourly pay recorded', end=": ")
        else:
            hourly_pay_rate = 0
    except ValueError as err:
        hourly_pay_rate = 0
        print('Invalid input, pay rate recorded as 0')
    else:
        print(f'${hourly_pay_rate:,.2f} per hour')
    finally:
        print(' ')
    print(f'{name.capitalize()} worked {hours_worked} this week with an hourly pay rate of ${hourly_pay_rate:,.2f}')


# when run the scrip this calls the function
if __name__ == '__main__':
    # calling the function
    hourly_employee_input()
"""
Tests:
1.)
Please enter your name: cOLbY
 
Enter hours worked: 35
Hours recorded: 35 hours worked
 
Enter your hourly pay rate: 20.182
Hourly pay recorded: $20.18 per hour
 
Colby worked 35 this week with an hourly pay rate of $20.18

2.)
Please enter your name: Colby
 
Enter hours worked: -9
0 hours worked
 
Enter your hourly pay rate: -9.5
$0.00 per hour
 
Colby worked 0 this week with an hourly pay rate of $0.00

3.)
Please enter your name: boell
 
Enter hours worked: -g
Invalid input, hours recorded as 0
 
Enter your hourly pay rate: j
Invalid input, pay rate recorded as 0
 
Boell worked 0 this week with an hourly pay rate of $0.00

"""
