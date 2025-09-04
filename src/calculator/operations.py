def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    # Kaitse 0-ga jagamise vastu
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def exponent(a: float, b: float) -> float:
    return a ** b

def modulus(a: float, b: float) -> float:
    # Kaitse 0-ga jäägi puhul
    if b == 0:
        raise ZeroDivisionError("Modulus by zero is not allowed.")
    return a % b
