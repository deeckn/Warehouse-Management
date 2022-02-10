import sqlite3
from log_entry import LogEntry


class LogDAO:

    __table_name = "LOG_ENTRIES"
    __COLUMN_ID = "id"
    __COLUMN_DATE = "date"
    __COLUMN_TIME = "time"
    __COLUMN_DESCRIPTION = "description"

    def __init__(self, connection: sqlite3.Connection):
        self.__connection = connection
        self.__cursor = self.__connection.cursor()
        self.__query_list = list()

    def get_all_log_entries(self) -> list[LogEntry]:
        """Retreives all log entries"""
        self.__cursor.execute(f"SELECT * FROM {LogDAO.__table_name}")
        users = self.__cursor.fetchall()
        self.__query_list = users
        self.__convert_to_object()
        return self.__query_list

    def __convert_to_object(self):
        """Converts raw data to User objects"""
        temp = list()
        for data in self.__query_list:
            log_entry = LogEntry(data[0], data[1], data[2], data[3])
            temp.append(log_entry)
        self.__query_list = temp

    def add_log_entry(self, log_entry: LogEntry):
        """Appends a log entry to the LOG_ENTRIES table"""
        self.__cursor.execute(f"""
            INSERT INTO {LogDAO.__table_name}
            ({LogDAO.__COLUMN_DATE}, {LogDAO.__COLUMN_TIME}, {LogDAO.__COLUMN_DESCRIPTION})
            VALUES ('{log_entry.get_date()}', '{log_entry.get_time()}', '{log_entry.get_description()}')
        """)
        self.__connection.commit()
