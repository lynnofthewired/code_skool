# Lynn Makowski
# Monkey Counter
# This program 

# the point at which the program stops printing, decrementing
NO_MONKEYS = 0

monkeys = input( int( "Good day, User! \nHow many monkeys are jumping on this bed?"))

while monkeys > NO_MONKEYS:
    print(f"{monkeys} little monkeys jumping on the bed. \n1 fell off and bumped their head. \nMama called the doctor, and the doctor said, \n\"no more monkeys jumping on the bed!\"")
    monkeys -= 1

print("Done!")