# Chapter 04: Quicksort — Lab Report

## Student Information
- **Name:** Owen Anthony Lee Chong
- **Date:** February 19, 2026

## Quicksort Concepts

### Divide and Conquer
Quicksort uses a divide-and-conquer strategy by picking a pivot element to partition an unsorted list into two smaller sub-arrays: elements less than the pivot and elements greater than it. You then recursively apply this same logic to each sub-array until they reach the base case of zero or one element, which is already sorted. Finally, the algorithm combines these sorted partitions with the pivot in the middle to return the complete, ordered list.

### The Three Steps
1. **Choose pivot:** The pivot is the central element chosen from the array (the first element in this lab) to act as a benchmark for partitioning.
2. **Partition:** This step reorganizes the array by comparing every other element against the pivot and grouping them into "less than" or "greater than" sub-arrays.
3. **Recurse and combine:** The function calls itself on the two piles and then joins the sorted piles back together with the pivot in the center.

## Tracing Quicksort

### Trace: quicksort([3, 5, 2, 1, 4])
quicksort([3, 5, 2, 1, 4])
  pivot = 3
  less = [2, 1]
  greater = [5, 4]

  quicksort([2, 1])
    pivot = 2
    less = [1]
    greater = []

    quicksort([1]) -> [1]  (Base case)
    quicksort([]) -> []    (Base case)

    result: [1] + [2] + [] = [1, 2]

  quicksort([5, 4])
    pivot = 5
    less = [4]
    greater = []

    quicksort([4]) -> [4]  (Base case)
    quicksort([]) -> []    (Base case)

    result: [4] + [5] + [] = [4, 5]

  Final Result: [1, 2] + [3] + [4, 5] = [1, 2, 3, 4, 5]

## Complexity Analysis

| Case | Time Complexity | Why? |
|------|----------------|------|
| Best | O(n log n) | Happens when the pivot splits the array into two nearly equal halves. |
| Average | O(n log n) | Most random cases provide a good enough split to maintain logarithmic depth. |
| Worst | O(n²) | Occurs on already sorted data with a first-element pivot, creating unbalanced partitions. |

## Reflection Questions

1. What happens if the array is already sorted and you always pick the first element as pivot?
If the array is already sorted and you consistently pick the first element as the pivot, the quicksort algorithm performs at its worst-case efficiency of O(n^2). This happens because each partition becomes extremely unbalanced, creating one empty list and one list containing all remaining n-1 elements. As a result, the recursion depth is maximized, significantly slowing down the process.

2. How could you improve pivot selection to avoid worst-case performance?
To avoid O(n^2) performance, you can implement randomized pivot selection by choosing a random index from the array instead of always using the first element. Alternatively, the "median-of-three" method picks the first, middle, and last elements and uses their median as the pivot to ensure more balanced partitions. These techniques help maintain the ideal O(n log n) time complexity.

3. How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)?
Quicksort is significantly more efficient than basic algorithms like bubble sort, which has a consistent O(n^2) time complexity. While merge sort also offers O(n log n) performance, quicksort is often faster in practice because it sorts "in-place" and has smaller constant factors. However, unlike merge sort, quicksort can degrade to O(n^2) if the pivot selection is poor.

4. Why do we use array[1:] instead of array when building the less and greater lists?
Using array[1:] ensures that the pivot itself is excluded from the comparison loop when building the new sub-partitions. If you included the whole array, the pivot would compare itself to itself and be placed back into the "less" list, potentially causing an infinite recursion loop. By slicing the array, you isolate the pivot and ensure the sub-problems are strictly smaller.