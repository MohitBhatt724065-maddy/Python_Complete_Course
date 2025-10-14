# Dunder method or Double underscore or constructor methods.
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def details(self):
        print(self.name)
        print(self.age)

p1 = person('Mike', 20)
p1.details()