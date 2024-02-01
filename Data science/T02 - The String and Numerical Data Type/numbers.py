
#user can you enter 3  three different intregers
enter_three_numbers = input("can you enter 3 different integers: ")

numbers = [int(num) for num in enter_three_numbers]
           
# im calculating and printing the outcome
print("sum of all numbers:", sum(numbers))
print("First number minus the second:", numbers[0] - numbers[1])
print("third number multipplied by the first:", numbers[2] * numbers[0])
print("The sum of all three numbers divided by the third number:", sum(numbers) / numbers[2])



