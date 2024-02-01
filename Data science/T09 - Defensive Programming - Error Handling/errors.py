print("Welcome to the error program")  # Syntax error: added parentheses, and =
print("\n")  # Syntax error: removed indentation, added parentheses

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24 years old"  # Syntax error: removed indentation and Run Time error: fixed removed extra =
age = int(age_str.split()[0])  # Syntax error: removed indentation and Type error : fixed by string slicing separate the numeric part and then convert it to an integer
print(f"I'm {age} years old.")  # Syntax error: removed indentation, added parentheses and Runtime error: fixed by using f string

# Variables declaring additional years and printing the total years of age
years_from_now = "3"  # Syntax error: removed indentation
total_years = age + int(years_from_now)  # Syntax error: removed indentation. Runtime error: fixed by converting year_from now to int

print("The total number of years: " + (total_years))  # Syntax error: added parentheses. Logical error: fixed by concatenating

# Variable to calculate the total amount of months from the total amount of years and printing the result
additional_months = 6
total_months = (total_years * 12) + additional_months  # Logical error: fixed by adding additional months
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")  # Syntax error: fixed by adding parentheses and run time error: fixed convert total months to str


