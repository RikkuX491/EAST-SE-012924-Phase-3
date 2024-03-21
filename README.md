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

***

### INSERT INTO (Create)

1. In `lib/models/hotel.py`, add the following instance method code in the `Hotel` model (class):

```py
def save(self):
    """ Insert a new row with the name value of the current Hotel instance.
    Update object id attribute using the primary key value of new row.
    """
    sql = """
        INSERT INTO hotels (name)
        VALUES (?)
    """

    CURSOR.execute(sql, (self.name,))
    CONN.commit()

    self.id = CURSOR.lastrowid

    Hotel.all.append(self)
```

`CURSOR.execute(sql)` will execute the SQL statement to insert a new row with the name of "Marriott" for the hotel into the `hotel_reviews.db` database. `CONN.commit()` allows for the changes when inserting, updating, or deleting rows to be committed to the database. Without `CONN.commit()`, the new row will not be added to the `hotels` table.

Try to write the code for the `save()` instance method for the `Customer` model (class) in `lib/models/customer.py` and the `save()` instance method for the `Review` model (class) in `lib/models/review.py`!

2. In `lib/models/hotel.py`, add the following class method code in the `Hotel` model (class):

```py
@classmethod
def create(cls, name):
    """ Initialize a new Hotel instance and save the object to the database """
    hotel = cls(name)
    hotel.save()
    return hotel
```

The `create()` method will create a new `Hotel` instance and save it to the database.

Try to write the code for the `create()` class method for the `Customer` model (class) in `lib/models/customer.py` and the `create()` class method for the `Review` model (class) in `lib/models/review.py`!

***

### SELECT (Retrieve)

1. In `lib/models/hotel.py`, add the following class methods in the `Hotel` model (class):

```py
@classmethod
def instance_from_db(cls, row):
    """Return a Hotel object having the attribute values from the table row."""
    
    hotel = cls(row[1])
    hotel.id = row[0]
    return hotel

@classmethod
def get_all(cls):
    """Return a list containing a Hotel object per row in the table"""
    sql = """
        SELECT *
        FROM hotels
    """

    rows = CURSOR.execute(sql).fetchall()

    cls.all = [cls.instance_from_db(row) for row in rows]
    return cls.all
```

The `get_all()` method will retrieve all rows from the `hotels` table and create a Python object for each of the rows retrieved from the `hotels` table from the database. `instance_from_db()` is a helper class method that will create a `Hotel` instance from information from a row in the `hotels` table from the database.

2. In `lib/models/hotel.py`, add the following class method in the `Hotel` model (class):

```py
@classmethod
def find_by_id(cls, id):
    """Return a Hotel object corresponding to the table row matching the specified primary key"""
    sql = """
        SELECT *
        FROM hotels
        WHERE id = ?
    """

    row = CURSOR.execute(sql, (id,)).fetchone()

    if row:
        return cls.instance_from_db(row)
    else:
        return None
```

The `find_by_id()` method will retrieve the row from the `hotels` table with the specified `id` and create a Python object for the row retrieved from the `hotels` table from the database using the `instance_from_db()` helper class method if a matching row is found. If no row is found, `None` is returned.

***

### UPDATE

In `lib/models/hotel.py`, add the following instance method in the `Hotel` model (class):

```py
def update(self):
    """Update the table row corresponding to the current Hotel instance."""
    sql = """
        UPDATE hotels
        SET name = ?
        WHERE id = ?
    """
    CURSOR.execute(sql, (self.name, self.id))
    CONN.commit()
```

The `update()` method will update the row from the `hotels` table with the instance's `id`.

***

### DELETE

In `lib/models/hotel.py`, add the following instance method in the `Hotel` model (class):

```py
def delete(self):
    """Delete the table row corresponding to the current Hotel instance and remove it from the all class variable"""


    sql = """
        DELETE FROM hotels
        WHERE id = ?
    """

    CURSOR.execute(sql, (self.id,))
    CONN.commit()

    # Remove the instance from the all class variable
    Hotel.all = [hotel for hotel in Hotel.all if hotel.id != self.id]
```

The `delete()` method will delete the row from the `hotels` table with the instance's `id` and also remove it from the `all` class variable in the `Hotel` model (class).