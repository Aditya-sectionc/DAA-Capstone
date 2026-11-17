from typing import List
from .models import Parcel

def sort_parcels(parcels: List[Parcel]) -> List[Parcel]:
    """Stable sort: higher priority first, then earlier deadline, then lower weight."""
    return sorted(parcels, key=lambda p: (-p.priority, p.deadline, p.weight))
