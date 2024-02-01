"""
This calculates the total price of apples and oranges based on user input. 
The user is prompted to enter the prices of apples and oranges, and the script then 
converts the input values to floating-point numbers and calculates the total price 
by adding them. Finally, it displays the total price to the user.
"""
# Get the price of apples as user input
price_apple = input("Enter price of apples: ")

# Get the price of oranges as user input
price_orange = input("Enter price of oranges: ")

# Convert the input values to floating-point numbers for calculations
price_of_apples = float(price_apple)
price_of_orange = float(price_orange)

# Calculate the total price by adding the prices of apples and oranges
total_price = price_of_apples + price_of_orange

# Display the total price to the user
print("Your total is:", total_price)

