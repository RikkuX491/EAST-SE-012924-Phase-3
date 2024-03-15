import ipdb

class Animal:

    # Deliverable 3
    all = []
    
    # Deliverable 1
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        # Deliverable 3
        Animal.all.append(self)

    # Deliverable 2
    def make_animal_sound(self):
        print("Animal Sound!")

# Deliverable 4
class Dog(Animal):

    # Deliverable 7
    all = []
    
    # Deliverable 5
    def __init__(self, name, age, bark_volume = 3, obedience_level = 3):
        super().__init__(name, age)
        self.obedience_level = obedience_level
        self.bark_volume = bark_volume

        Dog.all.append(self)

    # Deliverable 6
    def make_animal_sound(self):
        print(f"Bark{'!' * self.bark_volume}")

# Deliverable 8
class Cat(Animal):

    # Deliverable 10
    all = []

    def __init__(self, name, age):
        super().__init__(name, age)

        # Deliverable 10
        Cat.all.append(self)
    
    # Deliverable 9
    def make_animal_sound(self):
        print("Meow!")