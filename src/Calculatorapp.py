import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Divised by Zero")
    else:
        return a / b
    
def log10(x):
    if x <= 0:
        raise ValueError("Undefined for non-positive values")
    else:
        return math.log10(x)
    
def square(x):
    return x ** 2

def sqrt(x):
    if x < 0:
        raise ValueError("Number must be non-negative")
    else:
        return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def percentage(x):
    return x / 100