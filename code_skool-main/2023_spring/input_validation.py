# Lynn Makowski
# Garbage Trapper for Golf Scores
# This program takes a golf score entries, makes sure they are within a threshold
# throws an error message and a new prompt is it is not, and tells the user if
# they are on par, or their distance from par.

# All holes in one
PERFECT = 18
# Disaster capacity
CAP = 99

# The par score
par = 72

# Get a golf score
points = int(input('Please enter your score: '))

# Trapper loop makes sure the input is not less than 18, nor greater than 99
while points < PERFECT or points > CAP:
    print(f'ERROR: your score is out of range [{PERFECT} - {CAP}]')
    points = int(input('Please enter your score again: '))

if points < par:
    points = par - points
    print(f"You scored {points} points below par!")
elif points > par:
    points = points - par
    print(f"You scored {points} points above par.")
else:
    print(f"Your score is on par!")

