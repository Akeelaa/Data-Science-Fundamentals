# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #syntax error. Fixed: adding quotations marks.
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has  {number_of_teeth} teeth" # Logical error. fixed: moving arround the variables and added f string.

print(full_spec) #SyntaxError. fixed: added brackets to full_spec.

