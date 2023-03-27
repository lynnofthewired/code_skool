# Lynn Makowski
# Count to 100 Using Modular Step Size
# 

# the count initializes at 0
INIT = 0

# the count finishes at 100
FINISH = 100

# gathers the user-inputted step size
step = int( input("Please pick a positive integer greater than zero to choose our step size for our counter:  "))

# error message
if step <= 0:
    print(f"Error: invalid step size. \nPlease choose any integer greater than zero.")

for i in range ({INIT}, {step}, {FINISH}):
    print (f "{i}")

print(f"{step}, ")