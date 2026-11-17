import csv
import time
from pathlib import Path
from .data_io import load_parcels, load_graph
from .sorting import sort_parcels
from .knapsack import optimize_packing
from .graph_algorithms import shortest_path
from .tsp import nearest_neighbor_tsp

ROOT = Path(__file__).resolve().parents[1]

def run():
    parcel_file = ROOT / "datasets" / "parcels.csv"
    graph_file = ROOT / "datasets" / "routes.csv"

    parcels = load_parcels(parcel_file)
    graph = load_graph(graph_file)
    capacity = 20

    print("=" * 70)
    print("MINI-COURIER PLANNER")
    print("=" * 70)

    t0 = time.perf_counter()
    ordered = sort_parcels(parcels)
    sort_time = time.perf_counter() - t0

    print("\n1. PRIORITIZED PARCELS")
    print(f"{'ID':<6}{'Destination':<12}{'Wt':>5}{'Priority':>10}{'Deadline':>10}{'Value':>8}")
    for p in ordered:
        print(f"{p.parcel_id:<6}{p.destination:<12}{p.weight:>5}{p.priority:>10}{p.deadline:>10}{p.value:>8}")

    t0 = time.perf_counter()
    selected, weight, value, dp = optimize_packing(ordered, capacity)
    knapsack_time = time.perf_counter() - t0

    print(f"\n2. PACKING PLAN (capacity = {capacity})")
    print("Selected:", ", ".join(p.parcel_id for p in selected))
    print("Total weight:", weight)
    print("Total value:", value)
    print("DP optimum:", dp[-1][-1])

    customers = sorted({p.destination for p in selected})

    print("\n3. DIJKSTRA SHORTEST PATHS FROM DEPOT")
    for customer in customers:
        dist, path = shortest_path(graph, "Depot", customer)
        print(f"Depot -> {customer}: distance={dist}, path={' -> '.join(path)}")

    t0 = time.perf_counter()
    route, route_distance, legs = nearest_neighbor_tsp(graph, "Depot", customers)
    tsp_time = time.perf_counter() - t0

    print("\n4. DELIVERY ROUTE (Nearest-Neighbor TSP)")
    print(" -> ".join(route))
    print("Total route distance:", route_distance)
    print("\nLegs:")
    for u, v, d, path in legs:
        print(f"{u} -> {v}: {d} km via {' -> '.join(path)}")

    print("\n5. RUNTIME")
    print(f"Sorting:   {sort_time:.8f} sec")
    print(f"Knapsack:  {knapsack_time:.8f} sec")
    print(f"TSP route: {tsp_time:.8f} sec")
    print("\nProject completed successfully.")

if __name__ == "__main__":
    run()
