# Giving default values to parameters while using magic methods.

class Students:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age
        
    def details(self):
        return f"{self.name} is {self.age} years old." # This will only return the value but not actually print.
        
s1 = Students()
s2 = Students("John", 20)
print(s1.details()) 
print(s2.details()) # Using print statement explicitly to print the details.