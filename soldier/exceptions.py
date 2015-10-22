class SoldierError(OSError):
    """
    Base Class for Soldier Errors
    """
    pass


class ProcessDoesNotExistError(SoldierError):
    """
    Raised when trying to kill an inactive process
    """
    pass


class TimeoutError(SoldierError):
    """
    Raised when a process takes longer to finish than required
    """
    pass
