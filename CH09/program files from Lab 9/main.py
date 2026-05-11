import heapq

# =============================================================================
# Dijkstra's Shortest Path — Interactive CLI (Integrated Version)
# =============================================================================

def get_nodes():
    """Prompt the user to enter node names one at a time."""
    print("=== Dijkstra's Shortest Path ===\n")
    print("Enter node names one per line.")
    print("Type 'done' when finished.\n")

    nodes = []
    while True:
        line = input("Node: ").strip()
        if line.lower() == "done":
            break
        if not line:
            continue
        if line in nodes:
            print(f"  '{line}' already added.")
            continue
        nodes.append(line)
        print(f"  Added: {line}")
    return nodes


def get_edges(nodes):
    """Prompt the user to enter a weight for each pair of nodes."""
    print("\nFor each pair of nodes, enter the edge weight if connected, or press Enter to skip.\n")
    graph = {n: {} for n in nodes}
    for i, frm in enumerate(nodes):
        for to in nodes[i + 1:]:
            raw = input(f"  {frm} <--> {to}  (weight or Enter to skip): ").strip()
            if raw == "":
                continue
            try:
                weight = float(raw)
                graph[frm][to] = weight
                graph[to][frm] = weight
                print(f"    Added: {frm} <--{raw}--> {to}")
            except ValueError:
                print("    Skipped (not a number).")
    return graph


def draw_ascii_graph(graph, nodes, path_edges=None, start=None, end=None, path=None):
    """Print an ASCII representation of the graph to the console."""
    if path_edges is None:
        path_edges = set()
    col_w = 12

    def node_label(n):
        return f"[{n}]" if path and n in path else f"({n})"

    print("\n" + "─" * 52)
    print("  GRAPH")
    print("─" * 52)

    any_edges = False
    seen = set()
    for frm in nodes:
        for to, weight in graph.get(frm, {}).items():
            pair = tuple(sorted([frm, to]))
            if pair in seen:
                continue
            seen.add(pair)
            any_edges = True
            on_path = (frm, to) in path_edges or (to, frm) in path_edges
            arrow = "<=>" if on_path else "<->"
            w_str = int(weight) if weight == int(weight) else weight
            line = f"  {node_label(frm):>{col_w}}  {arrow}  {w_str:<6}  {node_label(to)}"
            if on_path:
                line = f"\033[92m{line}\033[0m"
            print(line)

    if not any_edges:
        print("  (no edges)")
    print("─" * 52)
    if path:
        print("  [node] = on path    (node) = not on path    <=> = path edge")
    print()


def dijkstra(graph, nodes, start, end):
    """
    Dijkstra's using a Min-Heap (Priority Queue).
    Time Complexity: O(E log V)
    """
    costs = {node: float('inf') for node in nodes}
    costs[start] = 0
    parents = {node: None for node in nodes}
    
    # Priority Queue stores (cost, node)
    pq = [(0, start)]
    visited = set()

    while pq:
        current_cost, u = heapq.heappop(pq)

        if u in visited:
            continue
        if u == end:
            break
        
        visited.add(u)

        for v, weight in graph.get(u, {}).items():
            if v in visited:
                continue
            
            new_cost = current_cost + weight
            if new_cost < costs[v]:
                costs[v] = new_cost
                parents[v] = u
                heapq.heappush(pq, (new_cost, v))

    if costs[end] == float('inf'):
        return None, None

    # Reconstruct path
    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    path.reverse()

    return path, costs[end]


def main():
    nodes = get_nodes()
    if len(nodes) < 2:
        print("Need at least 2 nodes. Exiting.")
        return

    graph = get_edges(nodes)
    draw_ascii_graph(graph, nodes)

    print(f"Nodes: {', '.join(nodes)}")
    start = input("From: ").strip()
    end   = input("To:   ").strip()

    if start not in nodes or end not in nodes:
        print(f"Error: Node not found.")
        return

    path, total_cost = dijkstra(graph, nodes, start, end)

    if path is None:
        print(f"\nNo path found from '{start}' to '{end}'.")
        return

    path_edges = {(path[i], path[i + 1]) for i in range(len(path) - 1)}
    draw_ascii_graph(graph, nodes, path_edges=path_edges, start=start, end=end, path=path)

    print(f"  Shortest path: {' -> '.join(path)}")
    cost_str = int(total_cost) if total_cost == int(total_cost) else total_cost
    print(f"  Total cost:    {cost_str}\n")


if __name__ == "__main__":
    main()