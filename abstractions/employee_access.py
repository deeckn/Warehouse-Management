from access_level import AccessLevel


class EmployeeAccess(AccessLevel):
    def __str__(self) -> str:
        return "Employee Level Access"
