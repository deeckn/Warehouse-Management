from dataclasses import dataclass


@dataclass
class LogEntry:

    __id: int
    __date: str
    __time: str
    __description: str

    def get_id(self) -> int:
        return self.__id

    def get_date(self) -> str:
        return self.__date

    def get_time(self) -> str:
        return self.__time

    def get_description(self) -> str:
        return self.__description

    def get_data(self) -> tuple:
        return self.__date, self.__time, self.__description

    def __str__(self) -> str:
        return f"Date: {self.__date}, Time: {self.__time}, Description: {self.__description}"
