# Lecture # 7 - SQL Fundamentals & Table Relations

## Lecture Topics

- SQL statements
  - `CREATE TABLE table_name (id INTEGER PRIMARY KEY, column2 TEXT, column3 INTEGER);`
  - `ALTER TABLE table_name ADD COLUMN column4 TEXT;`
  - `DROP TABLE table_name;`
- SQL commands
  - `.help`
  - `.tables`
  - `.schema`
  - `.quit`
  - `.headers on` (Formats SQL output - output the name of each column)
  - `.mode column` (Formats SQL output - now we are in column mode, enabling us to run the next two .width commands)
  - `.width auto` (Formats SQL output - adjusts and normalizes column width)
- SQLite Data Types
  - `INTEGER`
  - `REAL`
  - `TEXT`
  - `NULL`
- Writing SQL statements to a File
  - Execute the code from the file in the terminal `sqlite3 example.db < example.sql`
- CRUD Operations in SQL
  - INSERT: `INSERT INTO table_name (column2, column3, column4) VALUES ('value1', 2, 'value3');`
  - SELECT (all rows and all columns): `SELECT * FROM table_name;`
  - SELECT (all rows and only column2 and column3): `SELECT column2, column3 FROM table_name;`
  - SELECT with WHERE (=): `SELECT * FROM table_name WHERE column2 = "value1";`
  - SELECT with WHERE value (<): `SELECT * FROM table_name WHERE column3 < 7;`
  - UPDATE: `UPDATE table_name SET column2 = "another value" WHERE column2 = "value1";`
  - DELETE: `DELETE FROM table_name WHERE id = 1;`
- Other SQL Queries
  - ORDER BY: `SELECT * FROM table_name ORDER BY column3;`
  - ORDER BY with DESC: `SELECT * FROM table_name ORDER BY column3 DESC;`
  - ORDER BY with LIMIT: `SELECT * FROM table_name ORDER BY column3 DESC LIMIT 1;`
  - BETWEEN: `SELECT * FROM table_name WHERE column3 BETWEEN 2 AND 4;`
- SQL Aggregate function (COUNT): `SELECT COUNT(column3) FROM table_name WHERE column3 = 2;`
- Primary Keys
- Foreign Keys
- SQL Joins
- Creating Join Tables

## Introduction

In today's lecture, we will discuss the SQL Fundamentals & Table Relations between tables in a relational database that we will build and interact with using SQL code.

## Setup

1. Run `sqlite3 hotel_reviews.db` in your terminal to enter the sqlite3 environment and begin writing SQL code to create tables and rows in the hotel_reviews database.