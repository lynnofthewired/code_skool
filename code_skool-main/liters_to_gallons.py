<<<<<<< HEAD
RATIO = 0.264172

def main():
    #REMEMBER TO COMMENT THESE VARIABLES
    liters = float(input("Enter the number of liters pumped: "))
    total_cost = float(input("Enter the total price to fill your tank: "))
    gallons = liters_to_gallons(liters)
    price = price_per_gallon(gallons, total_cost)

    print(f"You put {gallons:.3f} gallons of gas into your tank.")
    print(f"You paid the equivalent of ${price:.2f} per gallon.")

    liters_to_gallons(liters)

    price_per_gallon(gallons, total_cost)

# function to convert the liters input to a gallons quantity
def liters_to_gallons(liters):
    # Variable "gallons" is liters input multiplied by the ratio for conversion
    gallons = liters * RATIO
    # "gallons" is now the new value 
    return gallons

# function to convert price of the total in liters to a gallon equivalent
def price_per_gallon(gallons, total_cost):
    # Variable "price" is the total cost of the liters divided by the gallon measure
    price = total_cost / gallons
    # "price" gets this new value
    return price

=======
# Lynn Makowski
# Liters to Gallons Converter
# This program uses a basic algorithm for converting liters to gallons, and also
# the cost of a liter of gasoline, to determine the cost of a gallon of gasoline
# in cases where only the price per liter is known.

# Coefficient to determine the number of gallons you have in your total # of ltiers.
RATIO = 0.264172

def main():
    # User-input quantity of purchased liters
    liters = float(input("Enter the number of liters pumped: "))
    # User-input cost of the total ltiers
    total_cost = float(input("Enter the total price to fill your tank: "))

    # local variable, quantity of gasoline that will be printed when "main" is called,
    # calls a function which runs the algorithm
    gallons = liters_to_gallons(liters)

    # Local variable, price per gallon that will be printed when "main" is called, calls a function to get this value 
    price = price_per_gallon(gallons, total_cost)

    print(f"You put {gallons:.1f} gallons of gas into your tank.")
    print(f"You paid the equivalent of ${price:.2f} per gallon.")

def liters_to_gallons(liters):
    # Convert liters to gallons using the RATIO constant
    
    # Local variable gets result of algorithm for converting liters to gallons using the coefficient
    gallons = RATIO * liters
    # Passes the value from the algorithm into the "gallons" variable for when "liters_to_gallons"
    # is called in "main" resulting in this value being printed
    return gallons

def price_per_gallon(gallons, total_cost):
    # Local variable gets result of algorithm for converting cost of liters to cost of
    # gallons using the returned output from "liters_to_gallons"
    price = total_cost / gallons
    # Passes the value from the algorithm into the "price" variable for when "price_per_gallon"
    # is called in "main", resulting in this value being printed
    return price

# Call main
>>>>>>> 393dd49a0c37080e3e7a861c08c235c89775b0a4
main()