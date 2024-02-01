
star ="*"

# Iterate through each row  
for i in range (10): # # i = 0, i = 1, i = 2, etc. The variable i iterates from 0 to 9.
    if i <5:
  # If i is less than 5, print '*' repeated i times      
        print(i * star) 
        
    else:
    # If i is greater than or equal to 5, print '*' repeated (10 - i) times
        print((10 - i) * star ) # For example, when i = 7, print "*****"

