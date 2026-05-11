"""
Lab 2: Sorting Algorithms
Implements selection sort with performance tracking.
"""
from typing import List, Dict, Callable


def find_smallest_index(arr: List[Dict], key: Callable, start: int) -> int:
    """
    Find index of smallest element from start position.
    
    Args:
        arr: List to search
        key: Function to extract comparison value
        start: Starting index
    
    Returns:
        Index of smallest element
    """
    smallest_idx = start
    smallest_val = key(arr[start])
    
    for i in range(start + 1, len(arr)):
        if key(arr[i]) < smallest_val:
            smallest_val = key(arr[i])
            smallest_idx = i
    
    return smallest_idx


def selection_sort(arr: List[Dict], key: Callable = lambda x: x, reverse: bool = False) -> List[Dict]:
    """
    Sort list using selection sort algorithm.
    Time Complexity: O(n²)
    Space Complexity: O(1) - in-place sort
    
    Args:
        arr: List to sort
        key: Function to extract comparison value (default: identity function)
        reverse: If True, sort descending
    
    Returns:
        Sorted list (same list, modified in place)
    """
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    # Create a copy to avoid modifying original
    result = arr.copy()
    
    for i in range(n - 1):
        # Find smallest (or largest if reverse) in remaining portion
        if reverse:
            # Find largest
            extreme_idx = i
            extreme_val = key(result[i])
            for j in range(i + 1, n):
                comparisons += 1
                if key(result[j]) > extreme_val:
                    extreme_val = key(result[j])
                    extreme_idx = j
        else:
            # Find smallest
            extreme_idx = i
            extreme_val = key(result[i])
            for j in range(i + 1, n):
                comparisons += 1
                if key(result[j]) < extreme_val:
                    extreme_val = key(result[j])
                    extreme_idx = j
        
        # Swap if needed
        if extreme_idx != i:
            result[i], result[extreme_idx] = result[extreme_idx], result[i]
            swaps += 1
    
    print(f"Selection Sort: {comparisons} comparisons, {swaps} swaps")
    return result


def python_builtin_sort(arr: List[Dict], key: Callable = lambda x: x, reverse: bool = False) -> List[Dict]:
    """
    Python's built-in sort for comparison.
    Time Complexity: O(n log n) - Timsort algorithm
    """
    result = arr.copy()
    result.sort(key=key, reverse=reverse)
    print("Python Built-in Sort: O(n log n) - Timsort")
    return result
