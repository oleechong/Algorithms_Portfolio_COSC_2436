# Chapter 2: Selection Sort — Lab Report

## Student Information
- **Name:** Owen A LeeChong
- **Date:** February 02, 2026

## Algorithm Summary

### Selection Sort
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **How it works:** The algorithm divides the input list into two parts: a sorted sublist (built left to right) and a remaining unsorted sublist. It repeatedly finds the smallest (or largest) element in the unsorted sublist and swaps it with the leftmost unsorted element, moving the sublist boundary one element to the right.

## Array vs Linked List Analysis

| Operation | Array | Linked List | Why? |
|-----------|-------|-------------|------|
| Read      | O(1)  | O(n)        | Arrays allow random access via memory offsets; Linked Lists require traversing from the head. |
| Insert    | O(n)  | O(1)        | Arrays require shifting elements to make room; Linked Lists only require updating pointers (at the head).      |
| Delete    | O(n)  | O(1)        | Arrays require shifting elements to fill the gap; Linked Lists only require re-linking pointers.   |

## Test Results
main.py
Loaded 20 cities

============================================================
PART 1: SELECTION SORT
============================================================

Sorting cities by population (smallest first)...
Selection Sort: 190 comparisons, 10 swaps

Top 5 smallest cities:
  McAllen: 142,210
  Pasadena: 151,950
  Killeen: 153,095
  Brownsville: 183,392
  McKinney: 195,308

Sorting cities by population (largest first)...
Selection Sort: 190 comparisons, 0 swaps

Top 5 largest cities:
  Houston: 2,304,580
  San Antonio: 1,547,253
  Dallas: 1,304,379
  Austin: 978,908
  Fort Worth: 918,915

----------------------------------------
Comparison with Python's built-in sort:
Python Built-in Sort: O(n log n) - Timsort

============================================================
PART 2: ARRAY VS LINKED LIST
============================================================

--- Python List (Array) Operations ---
Array access by index [10]: 'Lubbock' - O(1) - 1.19 µs
Array insert at beginning: O(n) - 2.15 µs

--- Linked List Operations ---
Created linked list with 20 cities
LinkedList insert at head: O(1) - 2.62 µs

Searching for 'Dallas' in linked list...
LinkedList Search: Found in 4 comparisons

============================================================
PART 3: BIG O SUMMARY
============================================================
Selection Sort
O(n²): Each element is compared with every other element, leading to a quadratic number of comparisons.
Python's Timsort
O(n log n): Timsort is an efficient sorting algorithm based on merge sort and insertion sort, commonly used in Python's built-in sort.
Array vs Linked List
Array Operations:
Read: O(1)
Insert/Delete: O(n)
Linked List Operations:
Read: O(n)
Insert/Delete: O(1) at head

Using a dataset of 20 cities, the selection sort performed as follows:
Comparisons: 190
Swaps: Up to 19
Top 5 Smallest Cities identified: McAllen, Pasadena, Killeen, Brownsville, and McKinney.

By comparison, Python's built-in Timsort (O(n log n)) is significantly more efficient as the dataset grows, requiring only ~86 comparisons for the same 20 cities.

## Reflection Questions


1. Why is selection sort O(n²)?
   -It requires two nested loops. The outer loop runs (n) times (to place each element), and the inner loop searches the remaining unsorted list. On average, it checks (n²/2) elements for every outer loop iteration, leading to roughly (n²/2) operations.

2. When would you choose a linked list over an array?
   - A linked list is preferable when the application involves frequent insertions and deletions (especially at the beginning of the list) and the total number of elements are unknown or fluctuates significantly, as it avoids the O(n) "shifting" cost of an array.

3. Why does Python use arrays (lists) as the default sequence type?
   - Python lists are implemented as dynamic arrays because O(1) random access (reading/writing by index) is the most common operation in general programming. Additionally, modern CPUs are optimized for contiguous memory access, making arrays faster in practice due to cache locality.