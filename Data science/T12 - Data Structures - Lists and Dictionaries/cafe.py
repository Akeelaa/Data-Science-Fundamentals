

# I created a list of items on the cafes menu

menu = ["coffee", "pizza", "chips", "cake" ]

# I created a dictionary representing the stock of each item on the menu using key-value pairs

stock = {'coffee': 300, 'pizza': 400, 'chips': 200, 'cake': 100}

# I created a dictionary representing the price of each item on the menu using key-value pairs

price = {'coffee': 8, 'pizza': 15, 'chips': 3, 'cake': 10}

total_stock_value = 0

# This for loop will iterate each item in menu
for item in menu:

# This calculates the value of items by multipling the stock and price.

   item_value = stock[item] * price[item]

# Total stock value

   total_stock_value += item_value

# This will print the overall total stock value for all items on the menu.

print(f"Total stock value for all items is: {total_stock_value}")