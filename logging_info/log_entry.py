
class LogEntry:
    def __init__(self, date: str, time: str, description: str) -> None:
        self.date = date
        self.time = time
        self.description = description

    def get_date(self) -> str:
        return self.date

    def get_time(self) -> str:
        return self.time

    def get_description(self) -> str:
        return self.description

    def get_data(self) -> tuple:
        return self.date, self.time, self.description

    def __str__(self) -> str:
        return f"Date: {self.date}, Time: {self.time}, Description: {self.description}"
