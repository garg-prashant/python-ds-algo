"""
Module: tok_k_elements
License: MIT
Author: Prashant Garg
Date: 2025-08-10

Description:
------------
This module provides an implementation of finding the k largest and k smallest elements in an array, and searching in a heap.
"""

import heapq


def find_k_largest(arr: list[int], k: int) -> list[int]:
    """
    Find the k largest elements in an array.

    Parameters:
    ----------
    arr : list[int]
        The input array from which to find the k largest elements.
    k : int
        The number of largest elements to find.

    Returns:
    -------
    list[int]
        A list containing the k largest elements from the array.

    Time Complexity:
    ---------------
    O(n log k), where n is the number of elements in the array.

    Space Complexity:
    ----------------
    O(k), for storing the k largest elements.
    """
    if k == 0:
        return []
    return heapq.nlargest(k, arr)


def find_k_smallest(arr: list[int], k: int) -> list[int]:
    """
    Find the k smallest elements in an array.

    Parameters:
    ----------
    arr : list[int]
        The input array from which to find the k smallest elements.
    k : int
        The number of smallest elements to find.

    Returns:
    -------
    list[int]
        A list containing the k smallest elements from the array.

    Time Complexity:
    ---------------
    O(n log k), where n is the number of elements in the array.

    Space Complexity:
    ----------------
    O(k), for storing the k smallest elements.
    """
    if k == 0:
        return []
    return heapq.nsmallest(k, arr)


def search_in_heap(heap: list[int], value: int) -> bool:
    """
    Search for a value in a heap.

    Parameters:
    ----------
    heap : list[int]
        The heap in which to search for the value.
    value : int
        The value to search for.

    Returns:
    -------
    bool
        True if the value is found in the heap, False otherwise.

    Time Complexity:
    ---------------
    O(n), where n is the number of elements in the heap.
    """
    return value in heap


def main():
    """
    Main function to demonstrate finding k largest and k smallest elements,
    and searching in a heap.
    """
    arr = [11, 23, 3, 53, 32, 42, 22, 63, 3, 53, 33, 23, 45]
    k = 3
    print(f"k largest: {find_k_largest(arr, k)}, k={k}")
    print(f"k smallest: {find_k_smallest(arr, k)}, k={k}")

    # Demonstrate searching in a heap
    heap = arr[:]
    heapq.heapify(heap)
    value_to_search = 23
    print(f"Is {value_to_search} in heap: {search_in_heap(heap, value_to_search)}")


if __name__ == "__main__":
    main()
