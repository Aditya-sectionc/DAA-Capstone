from dataclasses import dataclass

@dataclass
class Parcel:
    parcel_id: str
    destination: str
    weight: int
    priority: int
    deadline: int
    value: int
