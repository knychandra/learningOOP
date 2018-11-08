class Fighters:
# here, fighers is a class

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    # name , age and weight here are the attributes that class(fighters) has

kenny = Fighters('Kenny', 20, 60)
everest = Fighters('Everest', 3, 15)

# here, kenny and everest are both an object of the class (fighters)
# it has class' attributes like name, age and weight

print(kenny.name)
print(kenny.age)
print(kenny.weight)

print(everest.name)
print(everest.age)
print(everest.weight)
