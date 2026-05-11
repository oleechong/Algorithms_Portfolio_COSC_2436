# Chapter 05: Hask Table — Lab Report

`## Student Information
- **Name:** Owen A LeeChong
- **Date:** 02/24/2026

## Key Concepts
In this lab, I implemented a Hash Table from scratch using Python. A hash table is a data structure that maps keys to values for highly efficient lookup. I used a hash function (utilizing the modulo operator %) to determine the index for each key. To handle cases where two keys map to the same index, I implemented Linear Probing, which is an open-addressing strategy that searches for the next available empty slot in the array.

## What I Learned
Through this lab, I gained a deeper understanding of:
Index Mapping: How to turn an arbitrary key (like a string) into a valid array index using hash() % size.
Collision Management: The necessity of logic to "probe" for the next spot when a collision occurs, ensuring data isn't overwritten.
Python Scoping: A reinforced lesson on how critical indentation is; specifically, ensuring method logic remains inside the def block to avoid SyntaxError.

## Challenges
The most difficult part was debugging the Indentation Errors. Initially, my while loops and return statements for the insert and search methods were not properly nested. This led to a return outside function error. I solved this by carefully re-aligning the code blocks. Additionally, ensuring the linear probing wrapped around to the start of the table using (index + 1) % self.size was a key logic hurdle that required careful tracing.

## Reflection Questions
1. **What are the advantages of using a hash table?** The primary advantage is speed. In an ideal scenario, hash tables provide O(1) (constant time) complexity for insertions and lookups. This makes them significantly faster than searching through a standard list (O(n)), especially as the dataset grows large. They are the backbone of high-performance tools like database indexes and caches.

2. **How does the hash function affect the performance of a hash table?** The hash function determines the distribution of data. A good hash function distributes keys uniformly across the table, minimizing collisions. If a hash function is poor and causes many keys to "cluster" at the same index, the performance degrades from O(1) toward O(n), as the program spends more time probing through occupied slots.

3. **What are other collision resolution techniques besides linear probing?** Quadratic Probing: Instead of checking the very next slot, it checks slots at an increasing interval (1, 4, 9, ...). This helps reduce primary clustering.Double Hashing: Uses a second hash function to determine the "step size" for probing, making the sequence unique to each key.Separate Chaining: Instead of finding a new slot in the main table, each index holds a Linked List. Multiple keys that hash to the same spot are simply appended to that list.
