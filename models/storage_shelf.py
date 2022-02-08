from dataclasses import dataclass


@dataclass
class StorageShelf:
    __id: int
    __label: str
    __max_weight: float
    __length: float
    __width: float
    __height: float
    __rows: int
    __columns: int

    def get_id(self) -> int:
        return self.__id

    def get_label(self) -> str:
        return self.__label

    def get_max_weight(self) -> float:
        return self.__max_weight

    def get_length(self) -> float:
        return self.__length

    def get_width(self) -> float:
        return self.__width

    def get_height(self) -> float:
        return self.__height

    def get_rows(self) -> int:
        return self.__rows

    def get_columns(self) -> int:
        return self.__columns
