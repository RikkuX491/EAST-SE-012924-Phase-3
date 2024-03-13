# Lecture # 3 - Object Oriented Programming in Python

## Lecture Topics

- Classes
- Instances
- Initializing with attributes using `__init__`
- Instance methods
- Self
- Object properties
- Using the `@property` decorator
- Modifying the `__repr__` instance method for a class

## Introduction

In today's lecture, we will discuss topics of Object Oriented Programming in Python such as classes, instances, `__init__`, attributes, instance methods, `self`, and object properties.

## Setup

1. Make sure that your current working directory (folder) contains a `Pipfile`, then run `pipenv install` in your terminal to install `pytest` and any other required packages.
2. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

## Deliverables

Write your code in `lib/car.py` (the `car.py` file in the `lib` directory / folder)

1. Create a `Car` class that takes in values for the following parameters for the `__init__` method: `make`, `model`, `year`. The `__init__` method should also take an optional value for the `horn_volume` parameter (set the default value for `horn_volume` to `1`).
2. Write the code to assign the values from the input parameters to the appropriate instance variables.
3. Create a property for the `year` instance variable. For the setter method, the `year` must be an `int` and must be between `1900` and `2023`. If it's not a valid `year`, raise a `ValueError` with the message "Year must be an integer and must be between 1900 and 2023!"
4. Create a property for the `horn_volume` instance variable. For the setter method, the `horn_volume` must be an `int`. If it's not a valid `horn_volume`, raise a `ValueError` with the message "Horn volume must be an integer!"
5. Create a property for the `make` instance variable. For the setter method, the `make` must be a `str` (string) that is at least 3 characters long. If it's not a valid `make`, raise a `ValueError` with the message "Make must be a string and must be at least 3 characters long!"
6. Make an instance method called `honk_horn` that will print a message in the following format: "BEEP BEEP!". The number of exclamation marks '!' should be dependent on the value for the `horn_volume` instance variable. So if `horn_volume` has the value of `3`. There should be 3 exclamation marks `!` after "BEEP BEEP".