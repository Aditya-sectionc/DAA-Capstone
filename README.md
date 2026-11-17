<<<<<<< HEAD
# DAA-Capstone
=======
# Mini-Courier Planner

## Capstone Assignment
This project implements an intelligent courier-planning prototype using:
- Sorting for parcel prioritization
- 0/1 Knapsack Dynamic Programming for box filling
- Dijkstra's Algorithm for shortest paths
- Nearest-Neighbor TSP approximation for delivery sequencing
- Runtime benchmarking for scalability analysis

## Project structure
```text
Mini-Courier-Planner/
├── src/
│   ├── main.py
│   ├── models.py
│   ├── sorting.py
│   ├── knapsack.py
│   ├── graph_algorithms.py
│   ├── tsp.py
│   └── data_io.py
├── datasets/
│   ├── parcels.csv
│   └── routes.csv
├── images/
├── screenshots/
├── mini_courier_planner.ipynb
├── report.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements
Python 3.10+ is recommended. The core implementation uses the Python standard library.

Install optional notebook/chart dependencies:
```bash
pip install -r requirements.txt
```

## Run
From the project root:
```bash
python -m src.main
```

## Algorithm summary
### 1. Parcel prioritization
Parcels are sorted by:
1. Higher priority first
2. Earlier deadline
3. Lower weight

Python's Timsort is used: average/worst-case O(n log n).

### 2. Box filling
A 0/1 Knapsack DP maximizes parcel value subject to the vehicle/box weight capacity.
Time: O(nW), Space: O(nW), where W is capacity.

### 3. Shortest path
Dijkstra's algorithm is used on the weighted customer graph.
With a binary heap: O((V+E) log V).

### 4. Route planning
Nearest-neighbor repeatedly chooses the closest unvisited customer using Dijkstra distances, then returns to the depot. This is a heuristic TSP approximation, not an exact optimal TSP solver.

## Sample result
The supplied dataset uses a box capacity of 20 units. The program prints:
- prioritized parcel list
- selected packing set
- total packed weight and value
- Dijkstra shortest paths
- final delivery route
- route distance
- component runtimes

## Complexity analysis
| Module | Algorithm | Time | Space |
|---|---|---:|---:|
| Prioritization | Timsort | O(n log n) | O(n) |
| Packing | 0/1 Knapsack DP | O(nW) | O(nW) |
| Shortest path | Dijkstra + heap | O((V+E)logV) | O(V+E) |
| Route | Nearest Neighbor + shortest paths | roughly O(k(V+E)logV) | O(V+E) |

## Limitations and future scope
- Nearest-neighbor does not guarantee an optimal TSP route.
- Current packing uses one capacity and one trip.
- Real systems should include vehicle location, traffic, time windows, fuel cost, multiple vehicles, and live delivery updates.
- Future work can use A*, OR-Tools, better TSP heuristics, multi-trip vehicle routing, and parallel route computation.

## GitHub submission
After testing:
```bash
git init
git add .
git commit -m "Initial capstone implementation"
git branch -M main
git remote add origin <YOUR_PRIVATE_REPOSITORY_URL>
git push -u origin main
git tag v1.0-final-submission
git push origin v1.0-final-submission
```
>>>>>>> 6e0f43b (Initial commit)
