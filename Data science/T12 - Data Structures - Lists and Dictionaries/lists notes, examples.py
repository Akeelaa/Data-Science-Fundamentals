
#why using lists are important:
#lists used to store a lot of data.
#list is a format of storing and organising datastring_list = ["Naruto", "Eren", "John"]
""""
string_list = ["Naruto" , "Eren", "John"]
print(string_list[2],string_list[0]) # can print multiple name through indexing 

#finding the length of a list
print(len(string_list))

#accessing all values in a list by using for loop

for i in string_list:
    print(i)
#another way to write the above 
for i in range (len(string_list)): #in this example 
    print(string_list[i])

#in operator and lists

#we can add new item to a list by using .append() will ONLY adds to the send of a list 
string_list.apend("sally")
print(string_list)
"""
# takes one element to the end
# we can .extend list which adds multiple values to the end only
"""
numbers = [1,2,3,4]
ex_numbers = [5,6,7,8, "true", "yes"]
numbers.extend(ex_number)
print(numbers)
"""

#inserting into list, we can inseert valies at a speciic postion
"""
numbers = [1,2,3,4,5]

numbers.insert(2, "Hi")
print(numbers)
"""
"""
#another example of insert new name 
name_list = ["john", "bill", "wick", "amy" ] 
name_list.insert(1, "tommy")
print(name_list)
"""
#popping from a list -remove a element at an index then return item
#



name_list = [
"john", 
"bill", 
"wick", 
"amy" 
] 
#popped can be used to update a list in data.
# used popped to Remove and store the first name (at index 0) in the list
popped_name = name_list.pop(0)
# Print the name that was removed
print(popped_name) 
# using Append to add a new name ("Johny") to the end of the list
name_list.append("Johny") 
#Print the updated list of names
print(name_list)
