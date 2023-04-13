# Lynn Makowski
# Budget Program with Exit Sentinel
# A budgeting program that gets a monthly budget and expense inputs
# until the user terminates the input loop. Then it does arithmetic
# and tells the user if the total expenses are within budget or not.

# Variable and prompt to initialize user's monthly budget
monthly = float( input( f"Good day, user! \nPlease state your monthly budget, and we can begin:  "))

# Sentinel variable
sentinel = float( input(f"You may begin entering expenses, and if there are none, or if you are finished, enter \"0\":  "))

# Variable for total input expenses
total = sentinel

# Get entries for expenses and total them into a variable
while sentinel != 0:
    sentinel = float( input(f"You may continuing entering expenses until you are finished, and then, enter \"0\":  "))
    total = total + sentinel

# Calculate budget difference
if total < monthly:
    monthly = monthly - total
    print (f"You have ${monthly:.2f} of unallocated funds.")
elif total == monthly:
    monthly = monthly - total
    print (f"You have met your monthly budget, with ${monthly:.2f} remaining.")
else:
    monthly = total - monthly
    print (f"Your expenses have exceeded your monthly budget by ${monthly:.2f}.")