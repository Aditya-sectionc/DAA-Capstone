from typing import List, Tuple
from .models import Parcel

def optimize_packing(parcels: List[Parcel], capacity: int) -> Tuple[List[Parcel], int, int, list]:
    """
    0/1 knapsack using dynamic programming.
    Returns selected parcels, total weight, total value, and the DP table.
    """
    n = len(parcels)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        p = parcels[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if p.weight <= w:
                candidate = dp[i - 1][w - p.weight] + p.value
                if candidate > dp[i][w]:
                    dp[i][w] = candidate

    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            p = parcels[i - 1]
            selected.append(p)
            w -= p.weight

    selected.reverse()
    total_weight = sum(p.weight for p in selected)
    total_value = sum(p.value for p in selected)
    return selected, total_weight, total_value, dp
