# Chapter 11: Dynamic Programming - The Knapsack Problem — Lab Report

## Student Information
- **Name:** Owen Anthony Lee Chong
- **Date:** April 21, 2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** Dynamic programming (DP) solves complex problems by breaking them down into simpler, overlapping subproblems and storing the results in a grid (memoization) to avoid redundant calculations. For the knapsack problem, the algorithm fills a table where each cell represents the maximum value achievable for a given weight capacity and a subset of items.
- **Time complexity:** The time complexity for this algorithm is O(n * w), where n is the number of items and w is the maximum weight capacity of the knapsack.
- **When to use it:** DP is best suited for optimization problems that exhibit "optimal substructure" and "overlapping subproblems," such as calculating the most valuable combination of goods to fit in a limited space.

## Test Results
The program successfully calculated the maximum value for a 4lb knapsack given a set of items (Guitar, Stereo, Laptop).

| Item | Weight | Value | Included in 4lb Max? |
| :--- | :---   | :---  | :---                 |
| Guitar | 1lb | $1,500 | Yes                  |
| Stereo | 4lb | $3,000 | No                   |
| Laptop | 3lb | $2,000 | Yes                  |
| **Total** | **4lb** | **$3,500** | **Optimal Result** |

## Reflection Questions

1. **Why is the grid system essential for the dynamic programming approach to the knapsack problem?**
   The grid allows the algorithm to track the "best" value for every increment of weight capacity, ensuring that when a new item is considered, we can easily compare its value plus the remaining capacity's best value against the previous best. Without the grid, we would be forced to re-calculate every possible combination, leading to exponential time complexity.

2. **What is the "formula" used to decide if an item should be added to the knapsack grid?**
   The algorithm compares the value of the previous "best" for that capacity against the value of the current item plus the best value that fits in the remaining space (Capacity - Current Item Weight). It chooses whichever of these two values is higher, ensuring that each cell in the grid always contains the most optimal solution found so far.

3. **How does dynamic programming differ from the greedy approach used in previous chapters?**
   A greedy algorithm makes the locally optimal choice at each step (like picking the most expensive item first), which doesn't always lead to the globally best solution. Dynamic programming, however, considers all sub-combinations through the grid system, guaranteeing an optimal global solution for the knapsack problem.

## Challenges Encountered
The primary challenge was managing the "off-by-one" errors when indexing the grid, especially when subtracting the current item's weight to find the remaining capacity. I resolved this by carefully tracing a small 3x3 grid by hand before implementing the nested loops in Python, which helped me visualize how the indices map to the weights.