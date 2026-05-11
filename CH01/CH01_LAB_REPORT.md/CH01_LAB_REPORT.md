# Chapter 1 Lab Report: Binary Search

## Student Information
- **Name:** Owen A LeeChong
- **Date:** Jan 25, 2026
- **Course:** COSC 2436

## Algorithm Summary

### Linear Search
Linear search is a straightforward approach that identifies a target value by examining every element in a sequence one by one from the start. This method is particularly useful when dealing with unsorted data or small lists where the time spent sorting would exceed the search time itself. Since the algorithm might need to scan the entire collection to find a match or confirm its absence, the time complexity is O(n). It remains a reliable fallback because it requires no prior organization of the dataset to function correctly.

### Binary Search
Binary search is a highly efficient algorithm that finds a target by consistently splitting a sorted list into two halves. By checking the middle element and discarding the half that doesn't contain the target, it rapidly narrows down the search area with each step. This "divide and conquer" logic gives it a time complexity of O(log n), making it ideal for processing massive datasets where a linear scan would be too slow. The only major constraint is that the data must be sorted beforehand, as the logic relies on numerical or alphabetical order to navigate.

## Test Results

[Binary Search vs Linear Search Time Comparison
================================================
Searching in a sorted list of 128 numbers

Searching for: 1
Linear search time: 0.00000215 seconds
Binary search time: 0.00000286 seconds
Linear search result: 0
Binary search result: 0
Binary search is 0.75x faster

Searching for: 64
Linear search time: 0.00000548 seconds
Binary search time: 0.00000191 seconds
Linear search result: 63
Binary search result: 63
Binary search is 2.88x faster

Searching for: 128
Linear search time: 0.00000334 seconds
Binary search time: 0.00000215 seconds
Linear search result: 127
Binary search result: 127
Binary search is 1.56x faster

Searching for: 50
Linear search time: 0.00000143 seconds
Binary search time: 0.00000095 seconds
Linear search result: 49
Binary search result: 49
Binary search is 1.50x faster

Searching for: 100
Linear search time: 0.00000334 seconds
Binary search time: 0.00000167 seconds
Linear search result: 99
Binary search result: 99
Binary search is 2.00x faster

Searching for: 25
Linear search time: 0.00000119 seconds
Binary search time: 0.00000072 seconds
Linear search result: 24
Binary search result: 24
Binary search is 1.67x faster

Searching for: 75
Linear search time: 0.00000215 seconds
Binary search time: 0.00000095 seconds
Linear search result: 74
Binary search result: 74
Binary search is 2.25x faster

Searching for: 10
Linear search time: 0.00000048 seconds
Binary search time: 0.00000072 seconds
Linear search result: 9
Binary search result: 9
Binary search is 0.67x faster

Searching for: 90
Linear search time: 0.00000215 seconds
Binary search time: 0.00000095 seconds
Linear search result: 89
Binary search result: 89
Binary search is 2.25x faster

Searching for: 200
Linear search time: 0.00000429 seconds
Binary search time: 0.00000143 seconds
Linear search result: None
Binary search result: None
Binary search is 3.00x faster

Lab Challenge Answer:
Maximum steps for binary search in 128 items:
log2(128) = 7 steps maximum]

