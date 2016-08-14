class SoldierError(OSError):
    """
    Base Class for Soldier Errors
    """
    pass


class InvalidCommandError(SoldierError):
    """
    Raised when an invalid command is encountered
    """
    pass


class ProcessDoesNotExistError(SoldierError):
    """
    Raised when trying to kill an inactive process
    """
    pass


class ProcessTimeoutError(SoldierError):
    """
    Raised when a process takes longer to finish than required
    """
    pass
