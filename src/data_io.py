import csv
from pathlib import Path
from .models import Parcel

def load_parcels(path):
    parcels = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            parcels.append(Parcel(
                parcel_id=row["parcel_id"],
                destination=row["destination"],
                weight=int(row["weight"]),
                priority=int(row["priority"]),
                deadline=int(row["deadline"]),
                value=int(row["value"])
            ))
    return parcels

def load_graph(path):
    graph = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            u, v, w = row["from"], row["to"], int(row["distance"])
            graph.setdefault(u, []).append((v, w))
            graph.setdefault(v, []).append((u, w))
    return graph
