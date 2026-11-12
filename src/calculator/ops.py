# Addition of two numbers
def add(a: float, b: float) -> float:
    return a + b

# Subtraction of two numbers
def subtract(a: float, b: float) -> float:
    return b - a

# Multiplication of two numbers
def multiply(a: float, b: float) -> float:
    return a * b

# Division of two numbers
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b