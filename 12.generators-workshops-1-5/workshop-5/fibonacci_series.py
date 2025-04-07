
from typing import Generator

def fibonacci_generator(start_a: int = 0, start_b: int = 1) -> Generator[int, None, None]:
    """A generator function for producing Fibonacci numbers starting from given values."""
    a, b = start_a, start_b
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_numbers(count: int) -> list[int]:
    """Return the first 'count' Fibonacci numbers as a list."""
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer.")
    fib_gen = fibonacci_generator()
    return [next(fib_gen) for _ in range(count)]


def fibonacci_up_to(limit: int) -> list[int]:
    """Generate Fibonacci numbers up to a given limit."""
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Limit must be a positive integer.")
    fib_gen = fibonacci_generator()
    result = []
    while (fib_num := next(fib_gen)) < limit:
        result.append(fib_num)
    return result


if __name__ == "__main__":
    print("Upto :",fibonacci_up_to(100))
    print("Count of numbers in series:", get_fibonacci_numbers(10))