
#asking user to enter sentence
str_manip = input("enter sentence: ")

#calculating the length of str.manip
length_of_str_manip = len(str_manip)
print("lenth of str_manip:", length_of_str_manip)

#im finding the last letter in str_manip
last_letter = str_manip[-1]
str_manip_edit = str_manip.replace(last_letter, "@")
print("edited str_manip: ", str_manip_edit)

#Im going to print the last 3 chracters in str_manip backwards
last_3_chracters = str_manip [-3:][::-1]
print("last 3 chracters backwards:", last_3_chracters)

#creating five letter words that is made of the first three characters and the last 2 chracters in str_manip
five_letter_word = str_manip[:3] + str_manip[::-1]
print("five letter word: ", five_letter_word)

