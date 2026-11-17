from heapq import heappush, heappop
from typing import Dict, List, Tuple

Graph = Dict[str, List[Tuple[str, int]]]

def dijkstra(graph: Graph, start: str):
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, u = heappop(pq)
        if dist != distances[u]:
            continue
        for v, weight in graph[u]:
            new_dist = dist + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                previous[v] = u
                heappush(pq, (new_dist, v))
    return distances, previous

def reconstruct_path(previous, start, target):
    if target == start:
        return [start]
    if previous.get(target) is None:
        return []
    path = []
    current = target
    while current is not None:
        path.append(current)
        if current == start:
            return path[::-1]
        current = previous[current]
    return []

def shortest_path(graph, start, target):
    distances, previous = dijkstra(graph, start)
    return distances[target], reconstruct_path(previous, start, target)
