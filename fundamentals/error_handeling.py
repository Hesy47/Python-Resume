class DivisionByZeroCustomError(Exception):
    def __str__(self):
        return "Can not divide by zero"


def divide(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers")

    if b == 0:
        raise DivisionByZeroCustomError

    return a / b


print(divide(10, 2))
# print(divide(1, 0))
# print(divide(1, "p"))


try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    result = first_number / second_number
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Invalid input, please enter numbers")
