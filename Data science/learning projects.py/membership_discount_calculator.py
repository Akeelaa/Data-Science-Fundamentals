"""
This code determines the discount percentage based on the user's age and membership status.
If the user is 60 years or older, a base discount of 20% is applied. If the user is also a member
of the rewards program, an additional 10% discount is added. The final discount percentage is
rounded and displayed to the user. Additionally, if the user is eligible for a discount but not
a rewards program member, they are encouraged to join the program for extra benefits.
"""


age = int(input("Please enter age:"))

# checking membership status yes or no.
is_member = input("Are you a member of our rewards programme? yes or no").lower()

#checking if user is a member and storing appropiate boolean

if is_member == "yes":
    is_member = True

else:
    is_member = False

# inaitilise discount variable
discount = 0.0

if age >= 60:
    discount = 0.2

# giving them a futher discount of 10%, thid eony excute if they are not a rewards memeber
    if is_member:
        discount += 0.1     # can be also written as discount = discount + 0.1 #errase

discount_per = discount * 100
rounded_discount = round(discount.per, 1)

print(f"Your discount percentage will be: {rounded_discount}%")

# eligibility  for discount
senior = discount > 0

# checking the logical operators to make sure it is correct. 
if senior and not is_member:
    print("Join our rewards programme for additional discounts!")
    # recommend rewards programme
