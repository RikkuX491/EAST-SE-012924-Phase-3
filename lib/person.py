import ipdb

class Person():

    all = []
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

        person_instances = [instance for instance in Person.all if type(instance) == Person]
        if(len(person_instances) == 0) and (type(self) == Person):
            self.id = 1
        else:
            self.id = person_instances[-1].id + 1

        Person.all.append(self)

    def speak(self):
        print("Hello World!")

    def __repr__(self):
        return f"Person # {self.id} - Name: {self.name}, Age: {self.age}"

class Adult(Person):

    all = []
    
    def __init__(self, name, age, job = "Student"):
        super().__init__(name, age)
        self.job = job
        
        if(len(Adult.all) == 0):
            self.id = 1
        else:
            self.id = Adult.all[-1].id + 1

        Adult.all.append(self)

    def speak(self):
        super().speak() # Hello World!
        print("I work for Flatiron School and it's great here!") # "I work for Flatiron School and it's great here!"

    def __repr__(self):
        return f"Adult # {self.id} - Name: {self.name}, Age: {self.age}, Job: {self.job}"

class Baby(Person):

    all = []
    
    def __init__(self, name, age, behavior_level = 3):
        super().__init__(name, age)
        self.behavior_level = behavior_level

        if(len(Baby.all) == 0):
            self.id = 1
        else:
            self.id = Baby.all[-1].id + 1

        Baby.all.append(self)

    def speak(self):
        print("Waaaaah!")

    def __repr__(self):
        return f"Baby # {self.id} - Name: {self.name}, Age: {self.age}, Behavior Level: {self.behavior_level}"

ipdb.set_trace()