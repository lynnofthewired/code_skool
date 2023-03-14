# Lynn Makowski
# Shipping Tables for Weights and Rates 
# A terminal printer that breaks down the totals for the costs of shipping packages. 

#The number of pounds the user's package weighs
pounds = float( input( "How many pounds, to the nearest tenth, does your package weigh?  "))

# The distance in miles that the item will be shipped
miles = int( input( "How many miles is the delivery?:  "))

# if logic for determining the delivery base rate, plus the distance coefficient
if pounds < 5:
    # Stores the delivery method, 1 or 2
    delivery_method = int( input( "Please select a delivery method; \"1\" for one-day shipping, or \"2\" for two-day.  "))
  # nested if logic, determines base rate and distance coefficient based on delivery method
    if delivery_method == 1:
      # Delivery base rate
      base_rate = 12.50
      # Distance coeff.
      shipping = .66 * miles
    else:
      base_rate = 8.75
      shipping = .45 * miles
  #the answer
# Same logic in the next range of values
elif pounds > 5 and pounds <= 20:
    delivery_method = int( input( "Please select a delivery method; \"1\" for one-day shipping, or \"2\" for two-day.  "))
    if delivery_method == 1:
      base_rate = 18.00
      shipping = .66 * miles
    else:
      base_rate = 11.50
      shipping = .45 * miles
  #the answer
elif pounds > 20 and pounds <= 50:
    delivery_method = int( input( "Please select a delivery method; \"1\" for one-day shipping, or \"2\" for two-day.  "))
    if delivery_method == 1:
      base_rate = 26.00
      shipping = .66 * miles
    else:
      base_rate = 20.50
      shipping = .45 * miles
  #the answer
else :
    delivery_method = int( input( "Please select a delivery method; \"1\" for one-day shipping, or \"2\" for two-day.  "))
    if delivery_method == 1:
      base_rate = 32.50
      shipping = .66 * miles
    else:
      base_rate = 25.00
      shipping = .45 * miles
  # the answer

# store the sum of base rate and the product of the distance in miles multiplied by the coefficient (.45, or .66)
cost = base_rate + shipping

# print the results
print(f"Base Rate:  ${base_rate:.2f} \nMileage: \t${shipping:.2f} \nTotal: \t\t${cost:.2f}"
)