# Mini-Courier Planner — Final Project Report

## 1. Problem Statement
The Mini-Courier Planner is a prototype that receives parcels and delivery points, prioritizes parcels, selects an optimized set that fits a delivery capacity, computes shortest paths, and produces an ordered delivery route.

The design integrates sorting, dynamic programming, graph algorithms, and approximation techniques.

## 2. Phase 1 — Courier Problem Design and Planning
### Parcel attributes
Each parcel contains:
- parcel_id
- destination
- weight
- priority
- deadline
- value

### Graph
The delivery network is represented as a weighted undirected adjacency list. Vertices represent the depot/customers and edges represent roads with distance weights.

### Integrated workflow
```text
Parcel Dataset
     |
     v
Priority Sorting
     |
     v
0/1 Knapsack DP
     |
     v
Selected Customers
     |
     v
Dijkstra Shortest Paths
     |
     v
Nearest-Neighbor TSP
     |
     v
Final Delivery Route
     |
     v
Runtime Analysis
```

## 3. Phase 2 — Package Prioritization and Box Filling
Parcels are sorted by descending priority, then ascending deadline and weight.

A 0/1 Knapsack DP is applied with a capacity of 20 units. Each parcel is either selected or not selected. The objective is to maximize total parcel value while keeping total weight within capacity.

The implementation also retains the DP table, which provides evidence of the optimization process.

## 4. Phase 3 — Route Maker and Graph Processing
Dijkstra's algorithm computes shortest paths from the depot to each selected customer.

The overall route uses a nearest-neighbor TSP heuristic:
1. Start at Depot.
2. Find the nearest unvisited customer using shortest-path distance.
3. Visit that customer.
4. Repeat until all selected customers are visited.
5. Return to Depot.

This reduces the route-planning problem to a practical heuristic instead of solving exact TSP, which becomes expensive as the number of locations increases.

## 5. Phase 4 — Performance Testing
The application records execution time for:
- parcel sorting
- knapsack optimization
- route planning

For a formal scalability experiment, run the notebook benchmark cells with increasing dataset sizes. Runtime should be reported in seconds and plotted against input size.

### Expected complexity
- Sorting: O(n log n)
- Knapsack: O(nW)
- Dijkstra: O((V+E) log V)
- Nearest-neighbor route planning: depends on the number of customers and shortest-path computations

## 6. Correctness Evidence
The console output demonstrates:
- sorted parcels
- selected parcels
- capacity constraint
- maximum DP value
- shortest paths
- final route
- total route distance
- runtime measurements

## 7. Optimization Discussion
Possible improvements include:
- replacing nearest-neighbor with 2-opt or stronger TSP heuristics
- caching repeated Dijkstra distances
- using a 1-D knapsack DP array when only the final optimum is required
- using A* when geographical coordinates and an admissible heuristic are available
- supporting multiple vehicles and delivery time windows

## 8. Conclusion
The project demonstrates how several algorithmic techniques can be integrated into one practical application. Sorting handles parcel prioritization, dynamic programming handles constrained package selection, Dijkstra handles shortest paths, and nearest-neighbor provides an efficient route approximation. Runtime measurements support discussion of scalability and algorithm selection.

## 9. Viva Questions
1. Why was sorting required?
2. Why is the packing problem a 0/1 Knapsack problem?
3. What does the DP table represent?
4. Why is Dijkstra suitable for positive road distances?
5. Why is nearest-neighbor called an approximation/heuristic?
6. Does nearest-neighbor always produce the optimal TSP route?
7. What happens if a customer is unreachable?
8. What is the time complexity of Dijkstra with a heap?
9. What is the effect of increasing knapsack capacity?
10. How could the project be extended to multiple delivery vehicles?
