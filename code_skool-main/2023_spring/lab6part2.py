# Lynn Makowski
# Monkey Counter
# This program fields a user for an integer, and uses that number to initialize the number
# of monkeys that start off jumping on the bed in the well-known nursery rhyme. The
# program then prints the whole nursery rhyme.

# the constant representing the point at which the program stops printing and decrementing,
# and terminates, because at 0, there are no monkeys
NO_MONKEYS = 0

# initialize the variable with the user input 
monkeys = int( input( "Good day, User! \nHow many monkeys are jumping on this bed?  "))

# error message
if monkeys < NO_MONKEYS:
    print(f"\nError: Please enter a positive integer.")

# while loop to decrement the user's integer to zero
while monkeys > NO_MONKEYS:
    print(f"\n{monkeys} little monkeys jumping on the bed. \n1 fell off and bumped their head. \nMama called the doctor, and the doctor said, \n\"No more monkeys jumping on the bed!\"")
    monkeys -= 1

# end of program
if monkeys == 0:
    print(f"\nNo monkeys jumping on the bed.")