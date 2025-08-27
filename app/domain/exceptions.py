class ItemNotFoundError(Exception):
    """Exception raised when an item is not found."""
    pass

class ItemAlreadyExistsError(Exception):
    """Exception raised when an item already exists."""
    pass