# Lynn Makowski
# Generation Sorter
# This program will tell the user what generation they are a part of based on
# the value of their input 

# integer variable from user input, to be run through if/else structure 
birth_year = int( input( "Please enter your birth year as a four-digit interval:  "))

# if/else structure associates ranges of years to various strings stored in the variable
if birth_year < 1900:
  message = "ERROR: Your entry is too early. Please enter a valid birth year."
elif birth_year >= 1900 and birth_year < 1922:
  message = "Your entry makes you Silent Generation."
elif birth_year >= 1922 and birth_year < 1946:
  message = "Your entry makes you War or Post-War Generation."
elif birth_year >= 1946 and birth_year < 1965:
  message = "Your entry makes you a Baby Boomer."
elif birth_year >= 1965 and birth_year < 1981:
  message = "Your entry makes you Gen X."
elif birth_year >= 1981 and birth_year < 1997:
  message = "Your entry makes you a Millennial."
elif birth_year >= 1997 and birth_year < 2012:
  message = "Your entry makes you Gen Z."
elif birth_year >= 2012 and birth_year < 2024:
  message = "Your entry makes you Gen Alpha."
else:
  message = "ERROR: Your entry is a future year. Please enter a valid birth year."

# now that the variable has the proper string, print that string
print(f"{message}")