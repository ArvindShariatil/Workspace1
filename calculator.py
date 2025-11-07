"""
A simple calculator module that provides basic arithmetic operations.
"""


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


"""def subtract(a, b):"""
    """Subtract b from a and return the result."""
   """ return a - b"""


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide a by b and return the result.
    
    Args:
        a: The dividend
        b: The divisor
    
    Returns:
        The quotient of a divided by b
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b and return the result."""
    return a ** b


def modulo(a, b):
    """Return the remainder of a divided by b.
    
    Args:
        a: The dividend
        b: The divisor
    
    Returns:
        The remainder of a divided by b
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot perform modulo with zero")
    return a % b
