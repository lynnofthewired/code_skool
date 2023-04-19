# A popular website offers a chocolate chip cookie recipe that produces 24 cookies per batch when baked properly. What if a user wanted to bake a differnt amount that 24 cookies? You are to write a Python program that helps the user convert the recipe to make more or less cookies. 

#The sugar cookie recipe requires the following ingredients:

#3 cups of flour
#0.75 cups of brown sugar
#2 eggs
#2 sicks of butter
#8 ounces of chocolate chips
#The recipe yeilds 24 cookies per batch.

#Write a program that does the following:

#Asks the user how many cookies they would like to make
#Converts the amounts needed for each ingredient based on the number of cookies input
#Hint: Create a variable that is a ratio of desired cookies to original cookie yield and use it as a multiplier on the original recipe ingredient values.

# The divisor derived from the number of cookies made by the original recipe.
OG_BATCH = 24
batch = int( input( "Good day, baker! How many cookies would you like to bake?  "))


og_flour = 3
og_brown_sugar = 0.75
og_eggs = 2
og_sticks_butter = 2
og_oz_chocolate_chips = 8

RATE_FLOUR = og_flour / OG_BATCH
RATE_SUGAR = og_brown_sugar / OG_BATCH
RATE_EGGS = og_eggs / OG_BATCH
RATE_BUTTER = og_sticks_butter / OG_BATCH
RATE_CHOCOLATE = og_oz_chocolate_chips / OG_BATCH

flour = RATE_FLOUR * batch
brown_sugar = RATE_SUGAR * batch
eggs = RATE_EGGS * batch
sticks_butter = RATE_BUTTER * batch
oz_chocolate_chips = RATE_CHOCOLATE * batch

print(f"{flour} cups of flower, \n{brown_sugar} cups of brown sugar, \n{eggs} eggs, \n{sticks_butter} sticks of butter, and {oz_chocolate_chips} ounces of chocolate chips.")

