#!/usr/bin/python3
"""Checks if object is an instance of a class"""

def is_same_class(obj, a_class):
    """
    returns True, if the object is an instanceof the class
    
    Args:
        obj: Any object to be checked
        a_class: The class to check against

    Returns:
        True if obj is an instance of a_class, otherwise False
    """

    return type(obj) is a_class
