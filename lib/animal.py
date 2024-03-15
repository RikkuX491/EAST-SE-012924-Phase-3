import ipdb

class Animal:

    all = []
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        Animal.all.append(self)

    def make_animal_sound(self):
        print("Animal Sound!")

class Dog(Animal):

    all = []
    
    def __init__(self, name, age, bark_volume = 3, obedience_level = 3):
        super().__init__(name, age)
        self.obedience_level = obedience_level
        self.bark_volume = bark_volume

        Dog.all.append(self)

    def make_animal_sound(self):
        # print("Bark" + f"{'!' * self.bark_volume}")
        print(f"Bark{'!' * self.bark_volume}")

class Cat(Animal):

    all = []

    def __init__(self, name, age):
        super().__init__(name, age)

        Cat.all.append(self)
    
    def make_animal_sound(self):
        print("Meow!")

animal1 = Animal("Alice", 2)
animal2 = Animal("Bob", 4)

fido = Dog("Fido", 3)
buddy = Dog("Buddy", 5, 4, 5)
cooper = Dog("Cooper", 4, 5)

kitty = Cat("Kitty", 4)
sally = Cat("Sally", 7)

ipdb.set_trace()