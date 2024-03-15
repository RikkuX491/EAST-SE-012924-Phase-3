# Lecture # 5 - Object Inheritance in Python

## Lecture Topics

- Object Inheritance
- `super()`

## Introduction

In today's lecture, we will discuss Object Inheritance in Python.

## Setup

1. Make sure that your current working directory (folder) contains a `Pipfile`, then run `pipenv install` in your terminal to install `pytest` and any other required packages.
2. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

## Deliverables

Write your code in `lib/animal.py` (the `animal.py` file in the `lib` directory / folder)

1. Define the `Animal` class such that an animal is initialized with a `name` and `age`. These should be saved as attributes within the `__init__()` method for the `Animal` class.

```py
animal1 = Animal("Alice", 2)

animal1.name
# "Alice"

animal.age
# 2
```

2. Create an instance method in the `Animal` class, `make_animal_sound()` that will print the following string to the console: "Animal Sound!"

```py
animal2 = Animal("Bob", 4)

animal2.make_animal_sound()
# "Animal Sound!"
```

3. Create a class attribute, `all`, in the `Animal` class. We will use this attribute to keep track of
the new `Animal` instances that are created from the `Animal` class. Set this
attribute equal to `[]`. Then in `__init__`, you will need to append the new `Animal` instances to the list contained within the `all` class attribute for the `Animal` class.

```py
animal1 = Animal("Alice", 2)
animal2 = Animal("Bob", 4)

Animal.all
# [<__main__.Animal object at 0x107c3d8b0>, <__main__.Animal object at 0x107b67820>]
```

4. Create and define a `Dog` class that inherits from the `Animal` class.

Note: Try creating a `Dog` instance in an `ipdb.set_trace()` session without passing in any arguments when creating the `Dog` instance. You'll notice that we get the following error, even though we haven't defined an `__init__` method for the `Dog` class:

```sh
TypeError: __init__() missing 2 required positional arguments 'name' and 'age'
```

This occurs because the `Dog` class inherits from the `Animal` class and will use the `Animal` class' `__init__` method by default! Since the `Animal` class requires us to pass in arguments for `name` and `age` when creating new `Animal` instances, we will need to pass in arguments for `name` and `age` when creating new `Dog` instances as well, since `Dog` inherits from the `Animal` class. In the next deliverable, we will be creating an `__init__` method for `Dog`, the child class which will allow for the child class to override the parent class' `__init__` method.

5. Create an `__init__()` method for the `Dog` class such that a `Dog` instance is initialized with a `name`, `age`, `bark_volume`, and `obedience_level`. `bark_volume` should be an optional parameter which has a default value of `1`, and `obedience_level` should be an optional parameter which has a default value of `3`. Use the `super()` function to call on the parent class' `__init__()` method (the `__init__()` method from the `Animal` class) and pass in `name` and `age` as arguments to the parent class' `__init__()` method. From there, the parent class' `__init__()` method will handle saving the `name` and `age` attributes for a new `Dog` instance. Save the `bark_volume` and `obedience_level` attributes within the `__init__` method for the `Dog` class.

```py
fido = Dog("Fido", 3)
buddy = Dog("Buddy", 5, 4, 5)

fido.name
# "Fido"

fido.age
# 3

fido.bark_volume
# 1

fido.obedience_level
# 3

buddy.bark_volume
# 4

buddy.obedience_level
# 5
```

6. Create an instance method in the `Dog` class, `make_animal_sound()` that will print the following string to the console: "Bark" followed by some exclamation marks `!` where the number of exclamation marks should be dependent on the value of the `bark_volume` for the `Dog` instance. For example, if the `Dog` instance's `bark_volume` is 3, the following string should be printed to the console: "Bark!!!"

```py
cooper = Dog("Cooper", 4, 5)

cooper.make_animal_sound()
# "Bark!!!!!"
```

7. Create a class attribute, `all`, in the `Dog` class. We will use this attribute to keep track of
the new `Dog` instances that are created from the `Dog` class. Set this
attribute equal to `[]`. Then in `__init__`, you will need to append the new `Dog` instances to the list contained within the `all` class attribute for the `Dog` class.

```py
fido = Dog("Fido", 3)
buddy = Dog("Buddy", 5, 4, 5)

Dog.all
# [<__main__.Dog object at 0x107b7ac70>, <__main__.Dog object at 0x107c3df10>]
```

8. Create and define a `Cat` class that inherits from the `Animal` class.

Note: Feel free to try creating `Cat` instances in an `ipdb.set_trace()` session, but remember to pass in arguments for `name` and `age` when creating new `Cat` instances since the `Cat` class inherits from the `Animal` class and will use the `Animal` class' `__init__` method by default!

9. Create an instance method in the `Cat` class, `make_animal_sound()` that will print the following string to the console: "Meow!"

```py
kitty = Cat("Kitty", 4)

kitty.make_animal_sound()
# "Meow!"
```

10. Create a class attribute, `all`, in the `Cat` class. We will use this attribute to keep track of
the new `Cat` instances that are created from the `Cat` class. Set this
attribute equal to `[]`. Then in `__init__`, you will need to append the new `Cat` instances to the list contained within the `all` class attribute for the `Cat` class.

```py
kitty = Cat("Kitty", 4)
sally = Cat("Sally", 7)

Cat.all
# [<__main__.Cat object at 0x107539a00>, <__main__.Cat object at 0x10761db50>]
```