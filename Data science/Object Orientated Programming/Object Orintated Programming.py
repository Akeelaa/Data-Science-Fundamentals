# Class is the blue print to the objecting im creating.

class Human:
    # self is a representation of an instance of an object
    def __init__ (self, name, age, height, gender=None): # attributes to my class

        self.name = name
        self.age = age
        self.height = height
        self.gender = gender

    # This temporary converts the Object into a string to view
    def __str__ (self):
    
        return f"""
    Human Name: {self.name}
    Humae Age: {self.age}
    Human Height: {self.height}
    Human Gender: {self.gender}

    """
Person1 = Human("John Wick", 28, 150)
Person2 = Human("Luke SKywalker", 23, 130)
Person3 = Human("Mr Robot", 28, 110)

print(Person1, Person2, Person3)
