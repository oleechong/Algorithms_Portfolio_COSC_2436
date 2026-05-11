# Lab 06: Breadth-First Search (BFS)

## Student Information
- **Name:** Owen Anthony Lee Chong
- **Date:** March 1, 2026

## Key Concepts
In this lab, I implemented the **Breadth-First Search (BFS)** algorithm to navigate a graph representing the Texas road network. Unlike depth-first strategies, BFS explores a graph **layer-by-layer**, starting from a source node and visiting all immediate neighbors before moving to the next level. This makes it the ideal algorithm for finding the **shortest path** in an unweighted graph (where every road/edge has an equal cost of 1). We represented this network using an **Adjacency List**, which is highly efficient for sparse graphs like a highway system.



## What I Learned
I gained a deeper understanding of how a **Queue (FIFO)** data structure dictates the behavior of the search. By enqueuing neighbors and marking them as "visited," I learned how to prevent infinite loops in a graph that contains cycles (like a circular highway loop). I also practiced back-tracking using a **predecessor map**, which allows the algorithm not just to find the target city, but to reconstruct the exact path taken from the start.

## Challenges
The most significant challenge was managing the visited set correctly while tracking the distance from the source. Initially, I had an issue where the algorithm would re-process nodes, leading to an inefficient O(V^2) runtime rather than the intended O(V + E). I solved this by ensuring a node is marked as visited the moment it is **enqueued**, rather than when it is dequeued. Another challenge was correctly parsing the Texas city data into the adjacency list to ensure all bidirectional roads were represented as two directed edges.



## Reflection Questions

### 1. Why does BFS use a queue instead of a stack?
A **Queue** follows a First-In-First-Out (FIFO) logic, which forces the algorithm to finish exploring all nodes at distance delta" before moving to any nodes at distance d+1. A stack (LIFO) would instead drive the search as deep as possible into one branch (DFS), failing to guarantee the shortest path.

### 2. What distinguishes BFS's shortest path from an actual shortest distance in a weighted graph?
BFS only calculates the shortest path based on the **number of edges** (hops). In a real-world Texas road network, the "shortest" path might have only 2 hops but cover 500 miles, while a 3-hop path might only cover 200 miles. For weighted distances (miles/time), an algorithm like **Dijkstra’s** would be required.

### 3. When would you choose BFS over DFS?
BFS is preferable when you need the shortest path in an unweighted graph or when the target is likely close to the source. DFS is more efficient for exploring all possible paths, detecting cycles, or when memory is limited (as BFS can have a very large "frontier" in memory).
