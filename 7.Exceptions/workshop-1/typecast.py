def divide_numbers(a, b):
    try:
        # Perform input validation
        result = a / b
        return result
    except ZeroDivisionError as exception:
        print(f"Error: Division by zero is not allowed. :: {exception}")
    except TypeError as exception:
        print(f"Error: Invalid operand types. :: {exception}")
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
print(divide_numbers(10, 2))  # Output: 5.0
print(divide_numbers(10, 0))  # Output: Error: Division by zero is not allowed.
print(divide_numbers("10", 2))  # Output: Error: Invalid operand types.
"""
catch three types of exceptions:

- ZeroDivisionError: This exception is raised when the divisor (b) is zero. In this case, we print an error message stating that division by zero is not allowed.

- TypeError: This exception is raised when the operands (a and b) have incompatible types for division. For example, if a is a string and b is an integer. In this case, we print an error message stating that the operand types are invalid.

- Exception: This is a generic exception that catches any other exception not explicitly caught by the previous two except blocks. In this case, we print a general error message along with the specific exception message.

The try-except block allows us to catch and handle exceptions gracefully, preventing the program from crashing and providing appropriate feedback to the user.

"""