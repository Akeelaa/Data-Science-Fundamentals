# Dictionaries consist of key-value pairs, similar to a list, but each item has two parts.

# Example dictionary with keys ("name", "age", "is_funny") and their corresponding values.
my_dictionary = {
    "name": "terry",
    "age": 23,
    "is_funny": False
}

popped = my_dictionary.pop("is_funny")
print(popped)

for i, j in my_dictionary.items(): # i = keys, j = values
    print(f"{i} : {j}")

my_dictionary['is_funny'] = popped
print(my_dictionary)

# To retrieve a value, reference the dictionary using the key.
reference = my_dictionary["age"]
print(reference)  # Output: 23

# Alternatively, you can use the get method to access a value by providing the key.
value = my_dictionary.get("name")
print(value)  # Output: terry




#we can use use the .item() method on a dictionary in a for loop to access both keys and values in dictionaries.

#we can also use .pop can use t0 remove a pair
