# Lynn Makowski
# Count to 100 Using Modular Step Size
# This program prompts the user for a step size in a counter that goes to 100, and will not go over.

# the count finishes at 100
MAX = 100

# gathers the user-inputted step size
step = int( input("Please pick a positive integer greater than zero to choose our step size for our counter:  "))

# variable is a sum of the initializer starts at the   
start = step

# the machine begins count at 0, so we want to increment the terminating constant one more time. 
finish = MAX + step

# do not output any value higher than the constant, MAX
if finish %= 0:
    finish = MAX + step
else finish = MAX

# error message
if step <= 0:
    print(f"Error: invalid step size. \nPlease choose any integer greater than zero.")

# for loop in three arguments, "start" is starting value, "finish" is our ending limit,
# and "step" is the step value.
for i in range (start, finish, step):
    # if, else logic ensures the message will print with proper punctuation.
    if i + step < finish:
        print(i, end=", ")
    else:
        print (i, end=".")