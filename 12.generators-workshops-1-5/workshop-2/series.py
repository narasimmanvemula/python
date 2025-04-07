"""
Encapsulation: Moved the logic for printing Fibonacci numbers into a separate function (print_fibonacci_numbers) for better modularity and reusability.
Comments: Added docstrings to explain the purpose of the generator and the printing function.
Main Guard: Included the if __name__ == "__main__": block to ensure the script can be imported without automatically executing the print logic.

"""
def fibonacci_generator():
    """A generator function for producing Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def print_fibonacci_numbers(count):
    """Print the first 'count' Fibonacci numbers."""
    fib_gen = fibonacci_generator()  # Create the Fibonacci generator
    for _ in range(count):
        print(next(fib_gen))

# Generate and print the first 10 Fibonacci numbers
if __name__ == "__main__":
    print_fibonacci_numbers(20)

