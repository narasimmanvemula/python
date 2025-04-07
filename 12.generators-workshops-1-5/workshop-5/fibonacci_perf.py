
import time
from fibonacci_series import get_fibonacci_numbers

def measure_fibonacci_performance(count: int) -> None:
    """Measure and print performance for generating 'count' Fibonacci numbers."""
    start_time = time.time()
    numbers = get_fibonacci_numbers(count)
    end_time = time.time()
    print(f"Generated {count} Fibonacci numbers in {end_time - start_time:.6f} seconds.")
    print(numbers)


if __name__ == "__main__":
    print("Performance Test:")
    measure_fibonacci_performance(1000)
