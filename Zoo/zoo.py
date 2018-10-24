class Animal:
    def __init__(self, name, number_of_legs, food, characteristic):
        self.name = name
        self.number_of_legs = number_of_legs
        self.food = food
        self.characteristic = characteristic

    def description(self):
        return self.name + " had " + self.number_of_legs + ", eat " + self.food + " legs and can " + self.characteristic

class Bird(Animal):
    def __init__ (self, name, number_of_legs, food, characteristic, can_fly):
        Animal.__init__(self, name, number_of_legs, food, characteristic)
        self.can_fly = can_fly

    def description_bird(self):
        if self.can_fly == "yes":
            return Bird.description(self) + " and it can fly"
        elif self.can_fly == "no":
            return Bird.description(self) + " and it can not fly"

class Mammal(Animal):
    def __init__ (self, name, number_of_legs, food, characteristic, swim):
        Animal.__init__(self, name, number_of_legs, food, characteristic)
        self.swim = swim

    def description_mammal(self):
        if self.swim == "yes":
            return Mammal.description(self) + " and it is marine mammal"
        elif self.swim == "no":
            return Mammal.description(self) + " and it is not marine mammal"

class Tiger(Animal):
    def __init__(self, name, number_of_legs, food, characteristic, endarged):
        Animal.__init__(self, "tiger", "4", "meat", "jump")
        self.endarged = "yes"

    def description_tiger(self):
        return Tiger.description(self) + " and is endarged."

animal = raw_input("Add animal: ")

def add_animal(animal):
    name = raw_input("Write animal name: ")
    number_of_legs = raw_input("Write number of legs: ")
    food = raw_input("Write food: ")
    characteristic = raw_input("Write characteristic: ")
    type = raw_input("Bird or Mammal: ")
    if type == "Bird":
        can_fly = raw_input("Can it fly: ")
        animal = Bird(name, number_of_legs, food, characteristic, can_fly)
        return animal.description_bird()
    elif type == "Mammal":
        swim = raw_input("Is it live in water habitat: ")
        animal = Mammal(name, number_of_legs, food, characteristic, swim)
        return animal.description_mammal()

tiger = Tiger("tiger", "4", "meat", "jump", "yes")

if animal == "Tiger":
    print Tiger.description_tiger(tiger)
else:
    print add_animal(animal)
