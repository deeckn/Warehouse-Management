from access_level import AccessLevel


class AdminAccess(AccessLevel):
    def __str__(self) -> str:
        return "Admin Level Access"
