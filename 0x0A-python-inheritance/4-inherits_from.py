#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ function that returns True or false if obj
    is an instance of a_class

    args:
        obj: object
        a_class: class whose instance to check

    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
