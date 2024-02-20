def lookup(obj):
    """
    Return a list of attributes and methods for the given object

    Args:
    obj: Any object for which to retrieve attributes and methods.
    Returns:
    List of attributes and method names.
    """

    return dir(obj)
