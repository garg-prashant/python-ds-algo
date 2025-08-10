"""
Module: fibonacci
License: MIT
Author: Prashant Garg
Date: 2025-08-10

Description:
------------
This module provides an implementation of the Fibonacci sequence using simple recursion, recursion with memoization, and top-down dynamic programming.
"""

from functools import lru_cache
import timeit


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using simple recursion.

    Parameters:
    ----------
    n : int
        The position in the Fibonacci sequence to calculate.

    Returns:
    -------
    int
        The nth Fibonacci number.

    Time Complexity:
    ---------------
    O(2^n), due to the exponential growth of recursive calls.

    Space Complexity:
    ----------------
    O(n), due to the recursion stack.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache(maxsize=None)
def fibonacci_with_memoization(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion with memoization.

    Parameters:
    ----------
    n : int
        The position in the Fibonacci sequence to calculate.

    Returns:
    -------
    int
        The nth Fibonacci number.

    Time Complexity:
    ---------------
    O(n), due to memoization reducing redundant calculations.

    Space Complexity:
    ----------------
    O(n), for the memoization cache and recursion stack.
    """
    if n <= 1:
        return n
    return fibonacci_with_memoization(n - 1) + fibonacci_with_memoization(n - 2)


def fibonacci_top_down(n: int) -> int:
    """
    Calculate the nth Fibonacci number using a top-down dynamic programming approach.

    Parameters:
    ----------
    n : int
        The position in the Fibonacci sequence to calculate.

    Returns:
    -------
    int
        The nth Fibonacci number.

    Time Complexity:
    ---------------
    O(n), due to the iterative calculation.

    Space Complexity:
    ----------------
    O(n), for the dp_table array.
    """
    if n <= 1:
        return n

    dp_table = [0] * (n + 1)
    dp_table[1] = 1

    for i in range(2, n + 1):
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

    return dp_table[n]


def fibonacci_efficient_space(n: int) -> int:
    """
    Calculate the nth Fibonacci number using a space efficient dynamic programming approach.

    Parameters:
    ----------
    n : int
        The position in the Fibonacci sequence to calculate.

    Returns:
    -------
    int
        The nth Fibonacci number.

    Time Complexity:
    ---------------
    O(n), due to the iterative calculation.

    Space Complexity:
    ----------------
    O(1), as only two variables are used.
    """
    if n <= 1:
        return n

    a, b = 0, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


def main():
    """
    Main function to demonstrate the performance of Fibonacci calculations.
    """
    n = 30
    result_fibonacci = fibonacci(n)
    result_fibonacci_with_memoization = fibonacci_with_memoization(n)
    result_fibonacci_top_down = fibonacci_top_down(n)
    result_fibonacci_efficient_space = fibonacci_efficient_space(n)

    print(f"Fibonacci({n}) using normal recursion: {result_fibonacci}")
    print(
        f"Fibonacci({n}) using recursion with memoization: {result_fibonacci_with_memoization}"
    )
    print(
        f"Fibonacci({n}) using top-down dynamic programming: {result_fibonacci_top_down}"
    )
    print(
        f"Fibonacci({n}) using bottom-up dynamic programming: {result_fibonacci_efficient_space}"
    )

    time_taken_fibonacci = timeit.timeit(
        f"fibonacci({n})", globals=globals(), number=10
    )
    time_taken_fibonacci_with_memoization = timeit.timeit(
        f"fibonacci_with_memoization({n})", globals=globals(), number=10
    )
    time_taken_fibonacci_top_down = timeit.timeit(
        f"fibonacci_top_down({n})", globals=globals(), number=10
    )
    time_taken_fibonacci_bottom_up = timeit.timeit(
        f"fibonacci_efficient_space({n})", globals=globals(), number=10
    )

    print(f"Time taken by normal recursion: {time_taken_fibonacci:.6f} seconds")
    print(
        f"Time taken by recursion with memoization: {time_taken_fibonacci_with_memoization:.6f} seconds"
    )
    print(
        f"Time taken by top-down dynamic programming: {time_taken_fibonacci_top_down:.6f} seconds"
    )
    print(
        f"Time taken by bottom-up dynamic programming: {time_taken_fibonacci_bottom_up:.6f} seconds"
    )

    # Calculate and display the speed difference in value and percentage
    speedup_memoization = time_taken_fibonacci / time_taken_fibonacci_with_memoization
    speedup_top_down = time_taken_fibonacci / time_taken_fibonacci_top_down
    speedup_bottom_up = time_taken_fibonacci / time_taken_fibonacci_bottom_up

    print(
        f"Speedup with memoization: {speedup_memoization:.2f}x ({(1 - 1/speedup_memoization) * 100:.2f}%)"
    )
    print(
        f"Speedup with top-down DP: {speedup_top_down:.2f}x ({(1 - 1/speedup_top_down) * 100:.2f}%)"
    )
    print(
        f"Speedup with bottom-up DP: {speedup_bottom_up:.2f}x ({(1 - 1/speedup_bottom_up) * 100:.2f}%)"
    )


if __name__ == "__main__":
    main()
