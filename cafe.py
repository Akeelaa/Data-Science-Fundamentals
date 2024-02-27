# cafe.py

# I created a list of items on the cafes menu
menu = ["coffee", "pizza", "chips", "cake" ]

# I created a dictionary representing the stock of each item on the menu using key-value pairs
stock = {'coffee': 300, 'pizza': 400, 'chips': 200, 'cake': 100}

# I created a dictionary representing the price of each item on the menu using key-value pairs
price = {'coffee': 8, 'pizza': 15, 'chips': 3, 'cake': 10}

# Function to calculate the total sales
def calculate_total_sales(items):
    total = 0
    for item in items:
        total += stock[item] * price[item]
    return total

# Call the function with the menu items
total_sales = calculate_total_sales(menu)
print(f"Total sales for all items is: {total_sales}")
