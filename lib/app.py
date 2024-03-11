import ipdb

# Deliverable 1
print("Hello Flatiron! Class is in session!")

# Deliverable 2
def add(num1, num2):
    if(type(num1) in [int, float]) and (type(num2) in [int, float]):
        return num1 + num2
    else:
        raise Exception

# Deliverable 3
def subtract(num1, num2):
    if(type(num1) in [int, float] and (type(num2) in [int, float])):
        return num1 - num2
    else:
        raise Exception
    
# Deliverable 4
def multiply(num1, num2):
    if(type(num1) in [int, float] and (type(num2) in [int, float])):
        return num1 * num2
    else:
        raise Exception
    
# Deliverable 5
def divide(num1, num2):
    if(type(num1) in [int, float] and (type(num2) in [int, float]) and (num2 != 0)):
        return num1 / num2
    else:
        raise Exception
    
# Deliverable 6
def calculator(operation, num1, num2):
    if(operation == "+"):
        return add(num1, num2)
    elif(operation == "-"):
        return subtract(num1, num2)
    elif(operation == "*"):
        return multiply(num1, num2)
    elif(operation == "/"):
        return divide(num1, num2)
    else:
        raise Exception
    
# Deliverable 7
def print_greeting_loop(greeting):
    for char in greeting:
        print(char)