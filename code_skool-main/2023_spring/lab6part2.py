# Lynn Makowski
# Monkey Counter
# This program 

# the point at which the program stops printing and decrementing, and terminates
# because at 0, there are no more monkeys
NO_MONKEYS = 0

# initialize the variable with the user input 
monkeys = int( input( "Good day, User! \nHow many monkeys are jumping on this bed?  "))

if monkeys < 0:
    print(f"\nThere cannot be fewer than 0 monkeys. Please enter a positive ingeter.")

# while loop to decrement the user's integer to zero.
while monkeys > NO_MONKEYS:
    print(f"\n{monkeys} little monkeys jumping on the bed. \n1 fell off and bumped their head. \nMama called the doctor, and the doctor said, \n\"No more monkeys jumping on the bed!\"")
    monkeys -= 1

# success check 
if monkeys == 0:
    print(f"\nNo monkeys jumping on the bed!")