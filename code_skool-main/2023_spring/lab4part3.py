# Lynn Makowski
# User-Inputted Integer Analysis
# This program asks a user to enter two numbers of their choice,
# and displays whether the numbers are equal, or which is
# greater, and if each number is even or odd

entry1 = int( input( "Please enter an integer:  "))
entry2 = int( input( "Please enter a second integer:  "))

# determine which variable represents the greater integer, or if they are equal, and
# tell the user
if entry1 - entry2 > 0:
    print (f"Your first integer, {entry1}, is greater in value than your second, {entry2}.")
elif entry1 - entry2 < 0:
    print (f"Your first integer, {entry1}, is lesser in value than your second, {entry2}.")
else:
    print (f"Both of your integers, {entry1} and {entry2}, are equal in value.")


# find the remainders, if any, of both variables after they're divided by 2
rem1 = entry1 % 2
rem2 = entry2 % 2

# use that remainder to tell the user if the integers are even or odd, i.e., a remainder
# of zero proves an even integer
if rem1 == 0:
    print (f"Your first choice, {entry1}, is an even number.")
else:
    print (f"Your first choice, {entry1}, is an odd number.")

if rem2 == 0:
    print (f"Your second choice, {entry2}, is an even number.")
else:
    print (f"Your second choice, {entry2}, is an odd number.")