"""
Lab 6: Breadth-First Search Implementation
Finds shortest path (by number of edges) in unweighted graph.
"""
from typing import List, Dict, Optional
from collections import deque
from graph import Graph

def bfs_find_path(graph: Graph, start: str, end: str) -> Optional[List[str]]:
    """
    Find shortest path from start to end using BFS.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    
    Returns:
        List of vertices forming the path, or None if no path exists
    """
    # TODO: Implement bfs_find_path
    # 1. Check if start or end is not in graph, return None if not
    # 2. Initialize a queue with (start, [start])
    # 3. Initialize visited set with start
    # 4. While queue is not empty, pop the queue
    # 5. If current vertex is end, return path
    # 6. For each neighbor of current, if not visited, add to queue from typing import Dict, List, Set
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjacency_list: Dict[str, List[str]] = defaultdict(list)
        self.vertices: Set[str] = set()

    def add_vertex(self, vertex: str) -> None:
        self.vertices.add(vertex)

    def add_edge(self, v1: str, v2: str) -> None:
        self.vertices.add(v1)
        self.vertices.add(v2)
        if v2 not in self.adjacency_list[v1]:
            self.adjacency_list[v1].append(v2)
        if v1 not in self.adjacency_list[v2]:
            self.adjacency_list[v2].append(v1)

    def display(self) -> None:
        print("\nGraph Adjacency List:")
        print("-" * 40)
        for vertex in sorted(self.vertices):
            neighbors = self.adjacency_list[vertex]
            print(f"{vertex}: {neighbors}")

def bfs_all_reachable(graph: Graph, start: str) -> Dict[str, int]:
    """
    Find all vertices reachable from start and their distances.
    
    Returns:
        Dict mapping vertex -> distance from start
    """
    # TODO: Implement bfs_all_reachable
    # 1. Check if start is not in graph, return empty dict if not
    # 2. Initialize distances dict with start at distance 0
    # 3. Initialize queue with start
    # 4. While queue is not empty, pop queue
    # 5. For each neighbor, if not in distances, set distance and add to queue
from typing import List, Dict, Optional
from collections import deque
from graph import Graph

def bfs_find_path(graph: Graph, start: str, end: str) -> Optional[List[str]]:
    if start not in graph.vertices or end not in graph.vertices:
        return None
    queue = deque([(start, [start])])
    visited = set(start)
    
    while queue:
        (current, path) = queue.popleft()
        for neighbor in graph.get_neighbors(current):
            if neighbor == end:
                return path + [end]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

def bfs_all_reachable(graph: Graph, start: str) -> Dict[str, int]:
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        for neighbor in graph.get_neighbors(current):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    return distances

def bfs_is_connected(graph: Graph, v1: str, v2: str) -> bool:
    return bfs_find_path(graph, v1, v2) is not None

def bfs_is_connected(graph: Graph, v1: str, v2: str) -> bool:
    """Check if path exists between two vertices."""
    # TODO: Implement bfs_is_connected
    # 1. Use bfs_find_path to check if path exists
    # 2. Return True if path exists, False otherwise
from graph import Graph, create_texas_road_network
from bfs import bfs_find_path, bfs_all_reachable

def main():
    # =========================================
    # PART 1: Create Road Network
    # =========================================
    print("=" * 60)
    print("PART 1: TEXAS ROAD NETWORK GRAPH")
    print("=" * 60)
    
    roads = create_texas_road_network()
    print(f"\nCreated graph with {len(roads)} cities")
    roads.display()
    
    # =========================================
    # PART 2: Find Shortest Paths
    # =========================================
    print("\n" + "=" * 60)
    print("PART 2: SHORTEST PATH (BFS)")
    print("=" * 60)
    
    # Houston to El Paso
    path = bfs_find_path(roads, "Houston", "El Paso")
    if path:
        print(f"\nRoute: {' → '.join(path)}")
    
    # Houston to McKinney
    print("\n" + "-" * 40)
    path = bfs_find_path(roads, "Houston", "McKinney")
    if path:
        print(f"\nRoute: {' → '.join(path)}")
    
    # =========================================
    # PART 3: Reachability
    # =========================================
    print("\n" + "=" * 60)
    print("PART 3: DISTANCES FROM HOUSTON")
    print("=" * 60)
    
    distances = bfs_all_reachable(roads, "Houston")
    
    print("\nCities by distance (edges) from Houston:")
    for dist in range(max(distances.values()) + 1):
        cities_at_dist = [c for c, d in distances.items() if d == dist]
        if cities_at_dist:
            print(f"  {dist} edge(s): {', '.join(sorted(cities_at_dist))}")
    
    # =========================================
    # PART 4: Key Concepts
    # =========================================
    print("\n" + "=" * 60)
    print("PART 4: BFS KEY CONCEPTS")
    print("=" * 60)
    print("""
    Why BFS finds shortest path:
    1. Explores ALL nodes at distance 1 first
    2. Then ALL nodes at distance 2
    3. And so on...
    
    First time we reach destination = shortest path!
    
    BFS uses a QUEUE (FIFO):
    - First In, First Out
    - Process nodes in order they were discovered
    
    Time Complexity: O(V + E)
    - Visit each vertex once: O(V)
    - Check each edge once: O(E)
    
    Note: BFS finds shortest path by NUMBER OF EDGES.
    For weighted graphs (actual distances), use Dijkstra's (Lab 9)!
    """)

if __name__ == "__main__":
    main()
