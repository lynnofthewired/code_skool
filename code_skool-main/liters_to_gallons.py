RATIO = 0.264172

def main():

liters = float(input("Enter the number of liters pumped: "))
total_cost = float(input("Enter the total price to fill your tank: "))

gallons = liters_to_gallons(liters)
price = price_per_gallon(gallons, total_cost)

print(f"You put {gallons:.1f} gallons of gas into your tank.")
print(f"You paid the equivalent of $ {price:.2f} per gallon.")

def liters_to_gallons(liters):
    # Convert liters to gallons using the RATIO constant
    gallons = liters * RATIO
    return gallons

def price_per_gallon(gallons, total_cost):
    # Calculate the price per gallon
    price = total_cost / gallons
    return price

main()