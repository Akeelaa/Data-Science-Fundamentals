

# the variables
sum = 0
count = 0

# this will ask user to enter a number Continuously ask the user to enter a number until they enter -1
while True:
    number = int(input("Please enter a number: "))

    # if the user enters -1 it will end the loop
    if number == -1:
        break

    # the users number will be added to the sum and increment the count
    sum += number
    count += 1

# this will calculate the average
if count > 0:
    average = sum / count
    print(f"The average of the numbers entered are: {average}")
