from dataclasses import dataclass


@dataclass
class StorageShelf:
    label: str
    max_weight: float
    length: float
    width: float
    height: float
    rows: int
    column: int
