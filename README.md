# Lecture # 6 - Object Relationships

## Lecture Topics

- Object Relationships in Python
- One-to-many
- Many-to-many

## Introduction

In today's lecture, we will discuss about Object Relationships in Python. We will discuss relationships of tables in a relational database and will use Python classes as representations of tables from a relational database.

## Setup

1. Make sure that your current working directory (folder) contains a `Pipfile`, then run `pipenv install` in your terminal to install the packages in the `Pipfile` into the pipenv virtual environment.
2. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

Please note that there are no tests to run in this lecture repository.

## Deliverables

Write your code in `lib/many_to_many.py` (the `many_to_many.py` file in the `lib` directory / folder)

### Initializers and Properties

#### Hotel

- `Hotel __init__(self, name)`
  - A hotel is initialized with a name.
- `Hotel property name`
  - Returns the hotel's name.
  - Names must be of type `str`.
  - Names must be between 5 and 20 characters, inclusive.
  - Should **be able** to change after the hotel is instantiated.

#### Customer

- `Customer __init__(self, first_name, last_name)`
  - Customer is initialized with a first name and a last name.
- `Customer property first_name`
  - Returns the customer's first_name.
  - First names must be of type `str`.
  - First names must be longer than 0 characters.
  - Should **not be able** to change after the customer is instantiated.
  - _hint: hasattr()_

- `Customer property last_name`
  - Returns the customer's last_name.
  - Last names must be of type `str`.
  - Last names must be longer than 0 characters.
  - Should **not be able** to change after the customer is instantiated.
  - _hint: hasattr()_

#### Review

- `Review __init__(self, hotel, customer, rating, text)`
  - Review is initialized with a `Hotel` instance, a `Customer` instance, a rating, and
    text.
- `Review property rating`
  - Returns the review's rating.
  - Ratings must be of type `int`.
  - Ratings must be between 1 and 5, inclusive.
  - Should **not be able** to change after the review is instantiated.
  - _hint: hasattr()_
- `Review property text`
  - Returns the review's text.
  - Texts must be of type `str`.
  - Texts must be between 3 and 40 characters, inclusive
  - Should **not be able** to change after the review is instantiated.
  - _hint: hasattr()_