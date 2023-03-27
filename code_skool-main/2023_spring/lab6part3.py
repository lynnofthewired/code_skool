# Lynn Makowski
# Count to 100 Using Modular Step Size
# 

# the count finishes at 100
MAX = 100

# gathers the user-inputted step size
step = int( input("Please pick a positive integer greater than zero to choose our step size for our counter:  "))

# variable is a sum of the initializer starts at the   
start = step

finish = MAX + 1

# error message
if step <= 0:
    print(f"Error: invalid step size. \nPlease choose any integer greater than zero.")

for i in range (start, finish, step):
    print (i)