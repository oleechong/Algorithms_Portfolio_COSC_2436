# Chapter 3: Recursion — Lab Report

## Student Information
- **Name:** Owen LeeChong
- **Date:** February 12,2026

## Recursion Concepts

### Two Parts of Every Recursive Function
1. **Base Case:**  Anchors a recursive definition so the process eventually stops instead of calling itself forever.
2. **Recursive Case:** The part of a function where it calls itself with a smaller or simpler version of the original input. This step is designed to gradually reduce the problem until it matches the base case, preventing an infinite loop and allowing the final result to be calculated as the calls "unwind"

### The Call Stack
The call stack is a "last-in, first-out" (LIFO) data structure that keeps track of the active function calls in a program. When a function is called, it is "pushed" onto the stack; once it finishes, it is "popped" off, allowing the computer to return to exactly where it left off.

For example, if you call factorial(3), the stack first pushes factorial(3), then factorial(2), and finally factorial(1) on top. Once factorial(1) hits the base case and returns a value, the stack begins "unwinding" by popping each function off in reverse order to calculate the final result.

## Function Analysis

| Function         | Base Case            | Recursive Case            | Time Complexity |
|------------------|----------------------|---------------------------|-----------------|
| countdown        | i <= 0               | countdown(i-1)            | O(n)            |
| fact             | x <= 1               | x * fact(x-1)             | O(n)            |
| recursive_sum    | empty list           | first + sum(rest)         | O(n)            |
| recursive_count  | empty list           | 1 + count(rest)           | O(n)            |
| recursive_max    | single item          | max(first, max(rest))     | O(n)            |

## Reflection Questions

1. What happens if you forget the base case?

If you forget the base case, the function will call itself infinitely because it never encounters a condition to stop. This leads to a RecursionError (or "stack overflow") as the computer's memory becomes exhausted by the ever-growing call stack.

2. Why is the naive Fibonacci implementation inefficient?

A naive recursive Fibonacci implementation is inefficient because it performs a massive amount of redundant work/processes by recalculating the same subproblems multiple times. This results in an exponential time complexity, causing the call stack to grow rapidly even for relatively small input values.

3. Draw the call stack for `fact(4)`.

 def fact(n): if n == 0: # base case return 1 return n * fact(n-1)  --- ## Call stack while descending (calls being made) Top of stack is at the bottom of each block (like most debuggers). [main] → fact(4)  <-- bottom (topmost frame) [main] → fact(4) → fact(3)  [main] → fact(4) → fact(3) → fact(2)  [main] → fact(4) → fact(3) → fact(2) → fact(1)  [main] → fact(4) → fact(3) → fact(2) → fact(1) → fact(0)  At fact(0) the base case returns 1. --- ## Call stack while unwinding (returns happening) Each frame returns to its caller: fact(0) returns 1 fact(1) returns 1 * 1 = 1 fact(2) returns 2 * 1 = 2 fact(3) returns 3 * 2 = 6 fact(4) returns 4 * 6 = 24 So the final result is 24, and the stack fully clears back to [main]. --- ### Compact view (expand → unwind) Calls: fact(4) → fact(3) → fact(2) → fact(1) → fact(0) Returns: 4*6 ← 3*2 ← 2*1 ← 1*1 ← 1 Result: 24