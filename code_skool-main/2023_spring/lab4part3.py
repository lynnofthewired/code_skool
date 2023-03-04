# Lynn Makowski
# User-Inputted Integer Analysis
# This program asks a user to enter two numbers of their choice,
# and displays whether the numbers are equal, or which is
# greater, and if each number is even or odd

#import math

num1 = int( input( "Please enter an integer:  "))
num2 = int( input( "Please enter a second integer:  "))

# determine which variable represents the greater integer, or if they are equal, and
# tell the user
if num1 - num2 > 0:
    print (f"Your first integer, {num1}, is greater in value than your second, {num2}.")
elif num1 - num2 < 0:
    print (f"Your first integer, {num1}, is lesser in value than your second, {num2}.")
else:
    print (f"Both of your integers, {num1} and {num2}, are equal in value.")


# find the remainders, if any, of num1 and num2 after they're divided by 2
num3 = num1 % 2
num4 = num2 % 2

# use that remainder to tell the user if the integers are even or odd, i.e., a remainder
# of zero proves an even integer
if num3 == 0:
    print (f"Your first choice, {num1}, is an even number.")
else:
    print (f"Your first choice, {num1}, is an odd number.")

if num4 == 0:
    print (f"Your second choice, {num2}, is an even number.")
else:
    print (f"Your second choice, {num2}, is an odd number.")