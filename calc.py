# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

def power(x, y):
    if x <=0:
        raise ValueError('Can not take power')
    return x ** y