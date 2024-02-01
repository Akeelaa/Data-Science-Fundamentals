
# im asking the user to enter thier age
age_str = input("please enter age:")

# im going to convert the string in integer
age =int(age_str)
print("you entered:", age)

# if user is over 100 years old, the out messae will sorry your dead.
if age > 100:
   print("sorry you're dead")

# If the user is 65 or older, output the message will say "Enjoy your retirement!"
elif age >=65:
   print("Enjoy your retirement" "!")

# If the user is 40 or over, output the message "You're over the hill."
elif age >= 40:
  print("You're over the hill")

# im using conditional statement here so if there are under 13 you will qulify for the kiddie discount 
elif age < 13:
     print("You qualify for kiddie discount")

# this conditional statement is about if  the user is 21 then it will say congrats on your 21st
elif age == 21:
  print("Congrats on your 21st" "!")

else:
   print("Age is but a number.")
   

   




