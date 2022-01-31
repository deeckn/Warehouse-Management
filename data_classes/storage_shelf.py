from dataclasses import dataclass


@dataclass
class StorageShelf:
    label: str
    max_weight: float
    length: float
    width: float
    height: float
    rows: int
    columns: int

    def get_label(self) -> str:
        return self.label

    def get_max_weight(self) -> float:
        return self.max_weight

    def get_length(self) -> float:
        return self.length

    def get_width(self) -> float:
        return self.width

    def get_height(self) -> float:
        return self.height

    def get_rows(self) -> int:
        return self.rows

    def get_columns(self) -> int:
        return self.columns
