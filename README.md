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