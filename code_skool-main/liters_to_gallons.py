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

main()