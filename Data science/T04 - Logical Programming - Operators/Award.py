#Triantonlon Programme

#This is asking the user to enter their times for the 3 activities in triathlon
swimming_time = float(input("Enter your swimming time:"))
cycling_time = float(input("Enter your cycling time:"))
running_time = float(input("Enter your running time:"))

# this will calculate the total time taken complete the triathlon
total_time_taken = swimming_time + cycling_time + running_time 
print("total time taken:", total_time_taken)

#This code will display an award depending on the total time taken - conditional statements
if total_time_taken <= 100:
    print("Award: Provincial Colours")

#This elif' stands for 'else if', checking if the total time is greater than 100 and less than or equal to 105
elif total_time_taken > 100 and total_time_taken <= 105: # I used the "and" operator which combines, 2 conditions, so in this case it checks if the total time is greater than 100 and less than or equal to 105
    print("Award: Provincial Half Colours")

#This elif' stands for 'else if', checking if the total time is greater than 105 and less than or equal to 110
elif total_time_taken > 105 and total_time_taken <=110:
    print("Award: Provincial Scroll")
else:
    print("No Award") 











