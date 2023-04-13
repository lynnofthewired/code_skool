# Lynn Makowski
# Count to 100 Using Modular Step Size
# This program prompts the user for a step size in a counter that goes to 100, and will not go over.

# the count finishes at 100
MAX = 100

# gathers the user-inputted step size
step = int( input("Please pick a positive integer greater than zero to choose our step size for our counter:\n"))

# error message
if step <= 0:
    print(f"\nError: invalid step size. \nPlease choose any integer greater than zero.\n")

# variable is a sum of the initializer starts at the   
start = step

# checking if variable step is a factor of constant MAX 
mod = MAX % step

# if, else structure:
# because the machine begins count at 0, any step that is a factor of MAX needs one more increment
# after the count is technically finished. To prevent the output from exceeding the MAX, the
# variable finish is created without that extra increment.
if mod != 0:
    finish = MAX
else:
    finish = MAX + step

# for loop in three arguments, "start" is starting value, "finish" is our ending limit,
# and "step" is the step value.
for i in range (start, finish, step):
    # if, else logic ensures the message will print with proper punctuation.
    if i + step < finish:
        print(i, end=", ")
    else:
        print (i, end=".")