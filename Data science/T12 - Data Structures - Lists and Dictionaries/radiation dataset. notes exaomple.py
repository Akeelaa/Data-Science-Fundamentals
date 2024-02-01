
#Example:calculating the average radiiation level from small data set
radiation_levels = [ 15, 18, 20, 14, 16]

#using for loop to calculate the total

total = 0 
for level in radiation_levels:
    total += level
average =  total / len(radiation_levels)
print("The average Radiation level is:", average)


#Data organisation and average calculation - using def calculate function
#For example: our scientist are looking at radiation level in difference locations/areas
#urban area and forest area, creating a dictionary to organise data, using keys : values

locations = {'Urban': [18,20,22], 'Forest': [12,14,15] }

#defining function to calculate average
def calculate_average(levels): #creating a fuction called calculate average defining steps you want your programme to carry out
    return sum(levels) / len(levels)
for locations, levels in locations.items(): #using .item to iterate through the pair values (keys-values) 
    print(f"{locations} Average Radiation Level is: {calculate_average(levels)}")


#another example
location = {'birmingham': [1,2,3], 'London': [4,5,6] }


def calculate_average (place):
    return sum(place) / len(place)
for location, place in location.items():
    print(f"{location} avarage radioation levels is: {calculate_average(place)}")



menu = ["coffee", "pizza", "chips", "cake" ]
stock = {'coffee': 300, 'pizza': 400, 'chips': 200, 'cake': 100}
price = {'coffee': 8, 'pizza': 15, 'chips': 3, 'cake': 10}

for key in menu:

    total_stock = stock[key]
    print(total_stock)
    



