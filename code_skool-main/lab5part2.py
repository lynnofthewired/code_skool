# Lynn Makowski
# Pick Three and See What Happens
# A logic machine to determine which number is the greatest, and printing that. 

# Our first variable, a user-inputted integer
a = int( input( "Good day, user! Please pick a number for variable A:  "))
# Second variable, a user-inputed integer
b = int( input( "Now please pick a number for variable B:  "))
# Third variable, the final user-inputted integer
c = int( input( "Now please pick a number for variable C:  "))

# if logic to find the greatest nubmer
if a > b:
  if a > c:
    print(f"{a}")
  else:
    print(f"{c}")
else:
  if b > c:
    print(f"{b}")
  else:
    print(f"{c}")