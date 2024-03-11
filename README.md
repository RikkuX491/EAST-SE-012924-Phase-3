# Lecture # 1 - Python Fundamentals

## Lecture Topics

- pipenv install
- pipenv shell
- pytest
- pytest -x
- Debugging with `print()` and `ipdb`
- Python data types (`str`, `int`, `float`, `bool`, `None`)
- Control Flow: Operators, Conditional Statements, Loops
- Functions in Python
- Using `raise Exception()` to raise an Exception
- Handling errors with `try:` and `except:`

## Introduction

Welcome to Python! In today's lecture, we will discuss the Python Fundamentals including important terminal commands, using `ipdb` for debugging, control flow, functions, and using `raise Exception()` to raise an Exception.

## Setup

1. Make sure that your current working directory (folder) contains a `Pipfile`, then run `pipenv install` in your terminal to install `pytest` and any other required libraries.
2. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.
3. Run `pytest` from inside of the `EAST-SE-012924-Phase-3` directory to run the tests (if you can see `lib`, `Pipfile`, `Pipfile.lock`, `pytest.ini`, and `README.md` in your current working directory, then you are in the correct directory), and begin working to pass the tests. You can also run `pytest -x` to run one test at a time.

## Deliverables

1. Use the `print()` function to print the string `Hello Flatiron! Class is in session!`
2. Create a function called `add()` that has two parameters. The value of the two parameters should be either integers or floats. The `add()` function should add the two numbers and return the sum of the two numbers. The `add()` function should raise an Exception (using `raise Exception`) if the value of either of the two parameters is not an integer or float value.
3. Create a function called `subtract()` that has two parameters. The value of the two parameters should be either integers or floats. The `subtract()` function should subtract the two numbers and return the difference of the two numbers. The `subtract()` function should raise an Exception (using `raise Exception`) if the value of either of the two parameters is not an integer or float value.
4. Create a function called `multiply()` that has two parameters. The value of the two parameters should be either integers or floats. The `multiply()` function should multiply the two numbers and return the product of the two numbers. The `multiply()` function should raise an Exception (using `raise Exception`) if the value of either of the two parameters is not an integer or float value.
5. Create a function called `divide()` that has two parameters. The value of the two parameters should be either integers or floats, and the value of the second parameter cannot be equal to 0. The `divide()` function should divide the two numbers and return the quotient of the two numbers. The `divide()` function should raise an Exception (using `raise Exception`) if the value of either of the two parameters is not an integer or float value, or if the value of the second parameter is equal to 0.
6. Create a function called `calculator()` that has three parameters. The value of the first parameter should be a string with the value of `+`, `-`, `*`, or `/` since it represents the operation to be performed on two numbers. The value of the second and third parameters should be either integers or floats. The `calculator()` function should perform the operation (`+`, `-`, `*`, or `/`) specified by the value of the first parameter on the second and third parameters (the numbers) and return the result. The `calculator()` function should raise an Exception (using `raise Exception`) if the first parameter has any other value that is not equal to `+`, `-`, `*`, or `/`.
7. Create a function called `print_greeting_loop()` that has one parameter which is a string. The `print_greeting_loop()` should print each character of the string separately.
- Hint 1: You can use the `print()` function to print a value.
- Hint 2: You can use a `for` loop to iterate through a string's characters.

---


| Python                                                                                               | Javascript                                                                                   |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| None                      | undefined/null    |
| &&                        | and               |
| \|\|                      | or                |
| True/False                | true/false           |
| ipdb.set_trace()          | debugger          |
| snake_case                | camelCase         |
| f"{interpolate}"    | \`${interpolate}\`       |
| "true result" if "condition" else "default result"   | "condition" ? "true result" : "default result"   |
| if...elif...else    | if...else if...else    |
| try...except... | try...catch...  |
| def:                     | function{}         |
| If a function has parameters you have to pass in arguments for those parameters (otherwise you can set a default) | If a function has parameters JavaScript will not throw errors if you do not pass in arguments for said parameters |
| Variables need to immediately be assigned a value when created | Variables do not need to be immediately assigned a value when created |