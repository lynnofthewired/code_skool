# Lynn Makowski
# Type Specified Cookie Scaler
# This program stores the original values of the ingredients of an ideal cookie
# into constants, and follows algorithms to scale up and down thrugh batch sizes.

# Constant representing the number of cookies made by the original ingredients' values
ORIG_RECIPE_BATCH = 24

# Constants representing the original ingredients' values
ORIG_FLOUR = 3
ORIG_BROWN_SUGAR = 0.75
ORIG_EGGS = 2
ORIG_STICKS_BUTTER = 2
ORIG_OZ_CHOCOLATE_CHIPS = 8


def main():
    # Local variable stores input from users do determine how many cookies they want, to be used
    # to find the ratio
    cookies_to_make = int(input("Good day, baker! How many cookies would you like to bake?  "))
  
    # Local variable for the ratio, with the type batch as the divisor, to become the coefficient
    # in the "adjust_ingredient" function
    ratio = cookies_to_make / ORIG_RECIPE_BATCH

    # Local variables to store the scaled values of the scaled batch, these call
    # "adjust_ingredients" and simply multiply the type values by the product of the new batch
    # divided by the type batch
    adj_flour = adjust_ingredient(ratio, ORIG_FLOUR)
    adj_brown_sugar = adjust_ingredient(ratio, ORIG_BROWN_SUGAR)
    adj_eggs = adjust_ingredient(ratio, ORIG_EGGS)
    adj_sticks_butter = adjust_ingredient(ratio, ORIG_STICKS_BUTTER)
    adj_oz_chocolate_chips = adjust_ingredient(ratio, ORIG_OZ_CHOCOLATE_CHIPS)
    
    # Print the outcomes in a column 
    print(f"{adj_flour} cups of flour \n{adj_brown_sugar} cups of brown sugar \n{adj_eggs} eggs \n{adj_sticks_butter} sticks of butter \n{adj_oz_chocolate_chips} ounces of chocolate chips.")

# Defining function that stores the product of the value of the type ingredients multiplied by
# the value of the ratio
def adjust_ingredient(ratio, original_ingredient):
    # The parameter to be passed into the ingredient variables while this function is being called
    adjusted_ingredient = ratio * original_ingredient
    # Passes the value of the "adjusted_ingredient" variable into the variable that calls
    # "adjusted_ingredient" function
    return adjusted_ingredient

# Call "main"
main()