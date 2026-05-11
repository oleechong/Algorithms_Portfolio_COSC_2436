# Chapter 9: Dijkstra's Shortest Path — Lab Report 

## Student Information
Name: Owen A LeeChong
Date: April 04, 2026

## Algorithm Analysis: Dijkstra's Algorithm

**What type of graph does this program build?**
This program builds an undirected, weighted graph.

**Why must all edge weights be non-negative for Dijkstra's to work?**
Dijkstra's is a "greedy" algorithm. It assumes that once a node is processed, the shortest path to it has been found. If a negative weight exists, a later path could technically "reduce" the cost of a node that was already finalized, making the algorithm's earlier decisions incorrect.
Time Complexity (with simple array scan for min-node): O(V^2)
Time Complexity (with a min-heap/priority queue): O(E log V)
Core Data Structures

Structure	    Variable Name	What It Stores
Adjacency dict	Graph	        A nested dictionary mapping each node to its neighbors and the weight of the connecting edge.
Cost table	    Costs	        Tracks the lowest known cumulative weight from the source node to every other node.
Parent table	Parents	        Stores the "predecessor" node for each vertex, allowing the path to be reconstructed.
Visited list	Processed	    A list (or set) of nodes whose shortest path from the source has been finalized.

Given nodes A, B, C, D and edges A-B(1), A-C(4), B-C(2), B-D(6), C-D(3), trace Dijkstra's from A to D:

Iteration	Current Node	costs[A]	costs[B]	costs[C]	costs[D]	processed
Init	        —				0	       ∞           ∞           ∞           []
1               A               0          1           4           ∞           [A]
2               B               0          1           3           7           [A,B]
3               C               0          1           3           6           [A,B,C]
4               D               0          1           3           6           [A,B,C,D]  
				
Shortest path A to D: A -> B -> C -> D
Total cost: 6

Reflection Questions

**Why does the algorithm initialize all node costs to infinity except the start node?**
Dijkstra's initializes node costs to infinity to serve as a mathematical placeholder for "unreachable," ensuring that any actual path discovered will be cheaper than the initial value. The start node is set to zero as a baseline because you're already at the origin, allowing the algorithm to "seed" its search from a known cost. During the relaxation step, this infinity ensures the first real route found is recorded, as any numerical weight is smaller than the infinite placeholder. Ultimately, this setup prevents the logic from accidentally favoring a low numerical default over a valid, higher-cost path.



**Why do we store edges in both directions (graph[a][b] and graph[b][a])? What would break if we only stored one direction?**

Storing edges in both directions is essential because this assignment models an "undirected graph", where every connection between nodes is bidirectional rather than a "one-way street." If you only stored one direction (e.g., graph[a][b]), the algorithm would treat the connection as a directed edge, making it impossible to traverse from "b" back to "a". This would break Dijkstra's algorithm by causing it to report valid paths as "unreachable" simply because the data structure lacks the symmetry of the physical graph. By recording both directions, you ensure the adjacency dictionary accurately reflects that travel is possible from either side of the edge.
The find_lowest_cost_node() function scans all nodes linearly. How would using a priority queue (min-heap) improve performance, and why does it matter for large graphs?
A priority queue improves performance by replacing a slow O(V) linear scan with an efficient O(log V) heap operation, allowing the algorithm to instantly identify the next node to process. For large graphs, this optimization shifts the total complexity from O(V^2) to O(E log V), which prevents the processing time from ballooning exponentially as more data is added.  This scalability is vital for massive datasets, such as global road networks, where evaluating every single node manually would make real-time pathfinding computationally impossible.



**If a negative edge weight were introduced (e.g., A-B with weight -3), explain how Dijkstra's algorithm could produce an incorrect result. What algorithm handles negative weights?**
Dijkstra's algorithm follows a greedy logic that assumes a node's shortest path is finalized the moment it is processed, but negative weights can create a cheaper "late-breaking" route that the algorithm is not designed to revisit. This leads to incorrect results because the algorithm won't backtrack to update a finalized node if a new path including a negative edge suddenly lowers the cumulative cost.  To solve this, the "Bellman-Ford algorithm" is used instead, as it repeatedly relaxes all edges to account for negative weights and can even identify negative cycles that would otherwise cause an infinite loop.

**How does the parents dictionary allow path reconstruction? Why do we reverse the path at the end?**
The "parents dictionary" functions like a trail of breadcrumbs by storing the immediate predecessor for each node discovered on the cheapest path. To reconstruct the route, the algorithm starts at the destination and "walks backward" through these parent links until it reaches the source node.  Because this backtracking retrieves nodes in a finish-to-start sequence, the resulting list must be reversed to restore the logical chronological order for the user. This final step ensures the output reflects the actual journey from the starting point to the destination rather than the reverse search order.

**What happens when the source and destination are in disconnected components of the graph? How does the code detect this?**
When the source and destination reside in disconnected components, the algorithm's exploration boundary never reaches the target node, leaving its cumulative weight at the initial "infinity" placeholder. The code detects this isolation by checking if the destination's cost remains float(inf) after all reachable nodes have been processed.  Because no "breadcrumbs" are laid down for unreachable nodes, the "parents" dictionary remains empty for that destination, signaling that the nodes exist on isolated "islands" within the graph. To handle this gracefully, the function returns "None" for both the path and total cost, allowing the program to report that no valid route exists.

