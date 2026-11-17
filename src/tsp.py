from typing import List, Tuple
from .graph_algorithms import shortest_path, Graph

def nearest_neighbor_tsp(graph: Graph, start: str, customers: List[str]):
    """Nearest-neighbor TSP approximation using Dijkstra shortest-path distances."""
    unvisited = set(customers)
    if start in unvisited:
        unvisited.remove(start)

    route = [start]
    total_distance = 0
    legs = []

    current = start
    while unvisited:
        best_node = None
        best_dist = float("inf")
        best_path = []
        for candidate in sorted(unvisited):
            dist, path = shortest_path(graph, current, candidate)
            if dist < best_dist:
                best_dist, best_node, best_path = dist, candidate, path

        if best_node is None or best_dist == float("inf"):
            raise ValueError(f"No reachable customer from {current}")

        legs.append((current, best_node, best_dist, best_path))
        total_distance += best_dist
        route.append(best_node)
        current = best_node
        unvisited.remove(best_node)

    # Return to depot
    dist, path = shortest_path(graph, current, start)
    if dist == float("inf"):
        raise ValueError(f"No return path from {current} to {start}")
    legs.append((current, start, dist, path))
    total_distance += dist
    route.append(start)

    return route, total_distance, legs
