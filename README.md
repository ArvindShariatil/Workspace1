# Workspace1
Test Workspace

## Calculator Application

A simple, interactive calculator application written in Python that supports basic arithmetic operations.

### Features

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Power (^)
- Modulo (%)
- Error handling for division and modulo by zero

### Usage

#### Interactive Mode

Run the calculator in interactive mode:

```bash
python3 main.py
```

This will launch an interactive menu where you can:
1. Select an operation
2. Enter two numbers
3. View the result
4. Perform more calculations or exit

#### Using the Calculator Module

You can also import and use the calculator functions in your own Python code:

```python
import calculator

# Addition
result = calculator.add(5, 3)  # Returns 8

# Subtraction
result = calculator.subtract(10, 4)  # Returns 6

# Multiplication
result = calculator.multiply(3, 7)  # Returns 21

# Division
result = calculator.divide(15, 3)  # Returns 5.0

# Power
result = calculator.power(2, 8)  # Returns 256

# Modulo
result = calculator.modulo(17, 5)  # Returns 2
```

### Running Tests

To run the unit tests:

```bash
python3 test_calculator.py
```

Or with verbose output:

```bash
python3 test_calculator.py -v
```

### Files

- `calculator.py` - Core calculator module with arithmetic functions
- `main.py` - Interactive calculator application
- `test_calculator.py` - Unit tests for the calculator module
