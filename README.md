# Lecture # 8 - Object-Relational Mapping

## Lecture Topics

- Connecting ORMs to DBs
- How to use data from a database to make Python objects

## Introduction

In today's lecture, we will discuss about Object-Relational Mapping to allow for Python to have a way to connect to our SQLite database and how to use data from an SQLite database to make Python objects.

## Setup

1. Make sure that your current working directory (folder) contains a `Pipfile`, then run `pipenv install` in your terminal to install the packages in the `Pipfile` into the pipenv virtual environment.
2. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

## Starter Code

You can run `python lib/debug.py` in the terminal to run the code in `debug.py` and enter an `ipdb` debugging session to test / debug your code written in the models.

```py
#!/usr/bin/env python3
import ipdb;

from models.__init__ import CONN, CURSOR
from models.hotel import Hotel
from models.customer import Customer
from models.review import Review

if __name__ == '__main__':
    # don't remove this line, it's for debugging!
    ipdb.set_trace()
```

In `lib/models/__init__.py`, you will notice that the following starter code has been included:

```py
import sqlite3

CONN = sqlite3.connect('hotel_reviews.db')
CURSOR = CONN.cursor()
```

`sqlite3.connect('hotel_reviews.db')` returns an sqlite3 Connection object that contains a connection to the `hotel_reviews.db` SQLite database. Storing this sqlite3 Connection object in a variable allows you to have a reference to the connection to the database.

We can call the `.cursor()` method on `CONN`, the variable containing the reference to the connection to the database, to get an sqlite3 Cursor object that will allow us to interact with the database and execute SQL statements. We'll store this sqlite3 Cursor object in a variable called `CURSOR` to make it easier to interact with the database.

In `lib/models/hotel.py`, `lib/models/customer.py`, and `lib/models/review.py`, you will notice that the following `import` statement has been included on line 1 in those files:

```py
from models.__init__ import CONN, CURSOR
```

We can access the constants within those files by adding the `import` statement before the class declaration.

## Code Along

### Creating the tables

1. In `lib/models/hotel.py`, add the following class method code in the `Hotel` model (class):

```py
@classmethod
def create_table(cls):
    """ Create a new table to persist the attributes of Hotel instances """
    sql = """
        CREATE TABLE IF NOT EXISTS hotels (
        id INTEGER PRIMARY KEY,
        name TEXT)
    """
    CURSOR.execute(sql)
```

`CURSOR.execute(sql)` will execute the SQL statement contained within the `sql` variable to create the `hotels` table in the `hotel_reviews.db` database.

2. In `lib/models/customer.py`, add the following class method code in the `Customer` model (class):

```py
@classmethod
def create_table(cls):
    """ Create a new table to persist the attributes of Customer instances """
    sql = """
        CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT)
    """
    CURSOR.execute(sql)
```

`CURSOR.execute(sql)` will execute the SQL statement contained within the `sql` variable to create the `customers` table in the `hotel_reviews.db` database.

3. In `lib/models/review.py`, add the following class method code in the `Review` model (class):

```py
@classmethod
def create_table(cls):
    """ Create a new table to persist the attributes of Review instances """
    sql = """
        CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        rating INTEGER,
        text TEXT,
        hotel_id INTEGER,
        customer_id INTEGER)
    """
    CURSOR.execute(sql)
```

`CURSOR.execute(sql)` will execute the SQL statement contained within the `sql` variable to create the `reviews` table in the `hotel_reviews.db` database.

***

### Dropping the tables

1. In `lib/models/hotel.py`, add the following class method code in the `Hotel` model (class):

```py
@classmethod
def drop_table(cls):
    """ Drop the table that persists Hotel instances """
    sql = """
        DROP TABLE IF EXISTS hotels;
    """
    CURSOR.execute(sql)
```

`CURSOR.execute(sql)` will execute the SQL statement to drop the `hotels` table from the `hotel_reviews.db` database.

2. In `lib/models/customer.py`, add the following class method code in the `Customer` model (class):

```py
@classmethod
def drop_table(cls):
    """ Drop the table that persists Customer instances """
    sql = """
        DROP TABLE IF EXISTS customers;
    """
    CURSOR.execute(sql)
```

`CURSOR.execute(sql)` will execute the SQL statement to drop the `customers` table from the `hotel_reviews.db` database.

3. In `lib/models/review.py`, add the following class method code in the `Review` model (class):

```py
@classmethod
def drop_table(cls):
    """ Drop the table that persists Review instances """
    sql = """
        DROP TABLE IF EXISTS reviews;
    """
    CURSOR.execute(sql)
```

`CURSOR.execute(sql)` will execute the SQL statement to drop the `reviews` table from the `hotel_reviews.db` database.