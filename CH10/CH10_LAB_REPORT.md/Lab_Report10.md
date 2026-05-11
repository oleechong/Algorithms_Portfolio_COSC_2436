# Chapter 10: Greedy Algorithms (Truck Packing) — Lab Report

## Student Information
**Name:** Owen A LeeChong  
**Date:** April 14, 2026  
**Algorithm Analysis:** Greedy Truck Packing Algorithm  

---

# Algorithm Understanding

**What type of problem is this algorithm solving?**  
This is a combinatorial optimization problem, specifically a variation of the Bin Packing Problem or the 0/1 Knapsack Problem. It seeks an approximation of the best way to fit items into a container with limited capacity.

**Is this greedy algorithm guaranteed to produce the optimal solution? Why or why not?**  
No. A greedy algorithm makes the best "local" choice at each step (taking the largest box available) without considering the "global" picture. It might take a large box that leaves a small amount of awkward, unusable space, whereas taking two medium boxes might have filled the truck perfectly.

**What is the greedy choice made in this algorithm?**  
The greedy choice is prioritizing volume. Specifically, the algorithm always chooses the largest remaining box that can fit into the current available volume.
---

# Implementation Questions

**Why do we sort the boxes in descending order of volume before packing?**  
Sorting in descending order ensures we address the most "difficult" items (the largest ones) first while the truck is empty. Large items are harder to fit later in the process when space is fragmented.

**What would happen if we sorted the boxes in ascending order instead?**  
The truck would fill up with many small items first. While this packs many individual boxes, it might leave no room for larger, high-volume items, potentially resulting in a lower total volume of cargo being transported.

**Why do we keep track of `used_volume`?**  
We track used_volume to ensure the program never exceeds the physical capacity of the truck. It acts as a running tally to validate if the next box in the sorted list can still fit before we "commit" it to the packed list.

---

# Extension: Dimension Constraints

**Why is checking only volume not sufficient for real-world packing?**  
Volume is just a number, but physical objects have shape. A truck might have enough total volume to hold a 20-foot ladder, but if the truck is only 10 feet long, the ladder physically cannot fit inside regardless of how much empty "volume" is left.

**Give an example where a box fits by volume but not by dimensions.**  
Imagine a truck that is 5 x 5 x 5 (Total Volume = 125). A box that is 10 x 1 x 1 has a volume of only 10. Even though 10 is much smaller than 125, the 10-foot length of the box won't fit inside the 5-foot length of the truck.

**How would you modify the algorithm to check dimension constraints before packing a box?**  
In the for loop, I would add a conditional check: if box.length <= truck_length and box.width <= truck_width and box.height <= truck_height. Only if the box passes all three dimension checks AND the volume check would it be added to the truck.

---

# Reflection Questions

**What is a limitation of this greedy approach? Provide a scenario where it fails to find the optimal solution.**  
Provide a scenario where it fails to find the optimal solution. A limitation is that it cannot "look ahead."

Scenario: 
Truck capacity is 10. Boxes available: one size 6, and two size 5s.
Greedy: Takes the 6 (largest), leaving 4 units of empty space.
Optimal: Would take the two 5s, filling the truck perfectly (10/10).

**How is this problem related to the Knapsack Problem?**  
In the Knapsack Problem, you try to maximize the "value" of items in a bag with a weight limit. In this truck problem, the "weight limit" is the truck's volume, and the "value" of each box is its own volume. We are trying to maximize the total volume packed.

**What type of algorithm would guarantee an optimal solution for this problem? What is the tradeoff?**  
 A Dynamic Programming algorithm or a Backtracking (Brute Force) algorithm would guarantee the optimal solution. The tradeoff is time and memory. Greedy algorithms are very fast O(n log n), while optimal algorithms can become extremely slow O(2^n) as the number of boxes increases.

**If the truck had weight limits in addition to volume, how would the algorithm need to change?**  
Each Box would need a weight attribute, and the truck would need a max_weight capacity. The if statement inside the loop would need to check both: if (used_volume + box.volume <= max_volume) and (used_weight + box.weight <= max_weight).

**Why are greedy algorithms often preferred despite not always being optimal?**  
They are preferred because they are efficient and "good enough." In logistics and real-time computing, getting a 95% efficient solution in 1 second is often much more valuable than waiting 5 hours for a 100% "perfect" solution.