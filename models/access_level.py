from abc import ABC


class AccessLevel(ABC):
    pass


class AdminAccess(AccessLevel):
    def __str__(self) -> str:
        return "Admin Level Access"


class EmployeeAccess(AccessLevel):
    def __str__(self) -> str:
        return "Employee Level Access"
